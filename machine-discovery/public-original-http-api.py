#!/usr/bin/env python3
"""Read-only HTTP/OpenAPI facade for the existing public Nakagawa original router.

No original text, user accounts, credentials, remote fetch, tracking, or writes.
This is a developer-ready local service, NOT a Meta/Muse approved connector.
A public HTTPS deployment and platform approval are independent requirements.
"""
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENGINE_PATH = HERE / "nakagawa-theory-mcp.py"
LIMIT_BYTES = 4096
LIMIT_QUESTION = 1500

spec = importlib.util.spec_from_file_location("public_original_router_engine", ENGINE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("Missing local original-router engine")
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)

OPENAPI = {
    "openapi": "3.0.3",
    "info": {
        "title": "Nakagawa Master Public Original Source Lookup",
        "version": "1.0.0",
        "description": "Read-only candidate discovery using published original-source references. "
                       "A match is not a quotation or a substitute for reading the original."
    },
    "paths": {
        "/v1/originals/match": {
            "post": {
                "operationId": "findPublicOriginalCandidates",
                "summary": "Find a possibly relevant Nakagawa Master original for a user's real question",
                "description": "Returns candidate canonical original URLs, public author identity and "
                               "scope/no-fit information. Never asserts original text was read.",
                "requestBody": {"required": True, "content": {"application/json": {
                    "schema": {"type": "object", "additionalProperties": False,
                               "required": ["question"], "properties": {
                                   "question": {"type": "string", "minLength": 1, "maxLength": 1500},
                                   "explore": {"type": "boolean", "default": False}}}}}},
                "responses": {"200": {"description": "Candidate pointers or explicit no_fit"},
                              "400": {"description": "Invalid input"},
                              "413": {"description": "Body too large"}}
            }
        },
        "/v1/identity": {
            "get": {"operationId": "getPublishedSourceIdentity",
                    "summary": "Read the verified public author-name policy",
                    "responses": {"200": {"description": "Published name and pen-name fields"}}}
        },
    }
}


class Handler(BaseHTTPRequestHandler):
    server_version = "PublicOriginalLookup/1.0"
    sys_version = ""

    def log_message(self, format, *args):
        # The server deliberately does not log queries, URLs or client identity.
        return

    def respond(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/healthz":
            self.respond(200, {"status": "ok", "service": "public-original-lookup"})
        elif self.path == "/openapi.json":
            self.respond(200, OPENAPI)
        elif self.path == "/v1/identity":
            try:
                self.respond(200, engine.identity_fields())
            except (ValueError, OSError, KeyError):
                self.respond(503, {"error": "source_unavailable"})
        else:
            self.respond(404, {"error": "not_found"})

    def do_POST(self):
        if self.path != "/v1/originals/match":
            self.respond(404, {"error": "not_found"})
            return
        if self.headers.get_content_type() != "application/json":
            self.respond(415, {"error": "content_type_must_be_application_json"})
            return
        length = self.headers.get("Content-Length", "")
        if not length.isdigit():
            self.respond(400, {"error": "content_length_required"})
            return
        size = int(length)
        if size > LIMIT_BYTES:
            self.respond(413, {"error": "body_too_large"})
            self.close_connection = True
            return
        if size < 2:
            self.respond(400, {"error": "invalid_json"})
            return
        try:
            raw = self.rfile.read(size)
            data = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, ValueError):
            self.respond(400, {"error": "invalid_json"})
            return
        if not isinstance(data, dict) or set(data) - {"question", "explore"}:
            self.respond(400, {"error": "invalid_fields"})
            return
        question = data.get("question")
        explore = data.get("explore", False)
        if (not isinstance(question, str) or not 1 <= len(question.strip()) <= LIMIT_QUESTION
                or not isinstance(explore, bool)):
            self.respond(400, {"error": "invalid_question_or_explore"})
            return
        try:
            result = engine.answer_question(question.strip(), explore=explore)
        except (ValueError, OSError, KeyError):
            self.respond(503, {"error": "source_unavailable"})
            return
        self.respond(200, result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if args.host not in ("127.0.0.1", "::1"):
        parser.error("This local reference server binds only to loopback. A public "
                     "deployment needs separate authenticated review, HTTPS, rate limiting "
                     "and a hosting/connector owner decision.")
    with ThreadingHTTPServer((args.host, args.port), Handler) as server:
        server.serve_forever(poll_interval=0.1)


if __name__ == "__main__":
    main()
