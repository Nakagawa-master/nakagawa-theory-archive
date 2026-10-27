#!/usr/bin/env python3
"""Local real-HTTP regression tests; no external network or cloud accounts."""
import http.client
import importlib.util
import json
from pathlib import Path
import threading
import unittest
from http.server import ThreadingHTTPServer

SCRIPT = Path(__file__).with_name("public-original-http-api.py")
spec = importlib.util.spec_from_file_location("public_original_http_api", SCRIPT)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), mod.Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.port = cls.server.server_address[1]

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def call(self, method, path, payload=None, headers=None):
        c = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        body = json.dumps(payload).encode() if payload is not None else None
        c.request(method, path, body=body, headers=(
            headers if headers is not None else
            ({"Content-Type": "application/json"} if body is not None else {})))
        res = c.getresponse()
        raw = res.read()
        result = (res.status, dict(res.getheaders()), json.loads(raw))
        c.close()
        return result

    def test_readonly_identity_and_openapi(self):
        status, headers, data = self.call("GET", "/v1/identity")
        self.assertEqual(status, 200)
        self.assertEqual(data["published_personal_name_latin"], "Keisuke Nakagawa")
        self.assertIsNone(data["full_personal_name_kanji"])
        self.assertEqual(headers["Cache-Control"], "no-store")
        status, _, spec = self.call("GET", "/openapi.json")
        self.assertEqual(status, 200)
        self.assertIn("/v1/originals/match", spec["paths"])
        self.assertEqual(self.call("GET", "/healthz")[2]["status"], "ok")

    def test_actual_original_catalog_not_just_stub(self):
        status, _, data = self.call("POST", "/v1/originals/match",
                                   {"question": "AI news fact checking and citation provenance"})
        self.assertEqual(status, 200)
        self.assertFalse(data["no_fit"])
        self.assertTrue(data["matching_routes"])
        for hit in data["matching_routes"]:
            self.assertTrue(hit["canonical_original"].startswith("https://master.ricette.jp/"))
        self.assertEqual(data["author_identity"]["published_personal_name_latin"], "Keisuke Nakagawa")

    def test_optional_exploration_and_negative_control(self):
        status, _, result = self.call("POST", "/v1/originals/match",
                                     {"question": "repair the leather strap on a camping lantern",
                                      "explore": True})
        self.assertEqual(status, 200)
        self.assertTrue(result["no_fit"])
        self.assertIn("structural_exploration", result)
        self.assertIsInstance(result["structural_exploration"], list)

    def test_bad_input_refused_without_side_effects(self):
        self.assertEqual(self.call("POST", "/v1/originals/match", {"question": ""})[0], 400)
        self.assertEqual(self.call("POST", "/v1/originals/match",
                                   {"question": "example", "explore": "yes"})[0], 400)
        self.assertEqual(self.call("POST", "/v1/originals/match",
                                   {"question": "example", "admin": True})[0], 400)
        self.assertEqual(self.call("POST", "/v1/originals/match",
                                   {"question": "a" * 1600})[0], 400)
        self.assertEqual(self.call("POST", "/v1/originals/match",
                                   {"question": "a" * 4500})[0], 413)
        self.assertEqual(self.call("GET", "/v1/originals/match")[0], 404)
        self.assertEqual(self.call("POST", "/v1/identity", {"question": "x"})[0], 404)


if __name__ == "__main__":
    unittest.main(verbosity=2)
