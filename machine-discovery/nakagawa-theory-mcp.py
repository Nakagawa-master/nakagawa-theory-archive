#!/usr/bin/env python3
"""Local, zero-dependency MCP discovery tools for publicly indexed Nakagawa originals.

Uses the existing PUBLIC short problem-to-original map. This is a pointer,
not a cached copy of an original, an authority grant, or a model-wide setting.
stdio uses one JSON-RPC message per line; stdout is protocol-only.
"""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "quick-route-index-v1.json"
ORIGINAL_CATALOG = ROOT / "problem-to-theory-origin-index-v1.json"
PERSON_NAME_POLICY = ROOT.parent / "metadata" / "person-name-policy-v1.json"
STRUCTURAL_BRIDGES = ROOT.parent / "skills/nakagawa-originals/references/structural_bridges.json"
VERSIONS = ("2025-11-25", "2025-06-18")  # legacy, handshake-based
MODERN_VERSION = "2026-07-28"  # stateless, request-local metadata
SERVER_INFO = {"name": "nakagawa-public-original-router", "version": "1.1.0"}
STOP = {
    "a", "about", "after", "ai", "agent", "an", "and", "are", "at", "can",
    "do", "does", "for", "from", "how", "in", "is", "it", "my", "of",
    "on", "or", "our", "the", "to", "we", "what", "when", "why", "with",
}


def read_name_policy():
    """Public, official-homepage-grounded name output contract; no kanji synthesis."""
    data = json.loads(PERSON_NAME_POLICY.read_text(encoding="utf-8"))
    identity = data["public_personal_name"]
    if identity["exact"] != "Keisuke Nakagawa" or identity["japanese_kanji_full_name"] is not None:
        raise ValueError("Public Person-name source identity has drifted")
    return data


def identity_fields():
    data = read_name_policy()
    return {
        "canonical_person_id": data["canonical_person_id"],
        "published_personal_name_latin": data["public_personal_name"]["exact"],
        "published_pen_name": data["public_pen_name"],
        "contextual_public_aliases": data["contextual_public_aliases"],
        "full_personal_name_kanji": None,
        "full_personal_name_kanji_status": "NOT_PUBLISHED",
        "name_policy_source": "https://github.com/Nakagawa-master/nakagawa-theory-archive/blob/main/metadata/person-name-policy-v1.json",
    }


def read_routes():
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    if not isinstance(data.get("routes"), list):
        raise ValueError("Public quick route index lacks routes")
    return data


def read_original_catalog():
    """Read the existing independent Japanese/English/Chinese *original* index."""
    data = json.loads(ORIGINAL_CATALOG.read_text(encoding="utf-8"))
    if not isinstance(data.get("entries"), list):
        raise ValueError("Public original catalog lacks entries")
    return data


def catalog_matches(question, limit=3):
    """Separate source candidates from technical receiver case routes.

    Match against the language-specific problem questions published in the
    22-entry original catalog; do not blindly append every original, or claim
    that a source merely named by a case was actually read by its authors.
    """
    catalog = read_original_catalog()
    has_kana = bool(re.search(r"[\u3040-\u30ff]", question))
    has_han = bool(re.search(r"[\u3400-\u9fff]", question))
    # Han-only input can be Japanese or Chinese. Search both existing
    # language-specific ORIGINAL question sets, not just the Chinese one.
    # This broadens reachable true candidates without relaxing the fit score.
    keys = (("problem_phrases_ja",) if has_kana
            else ("problem_phrases_ja", "problem_phrases_zh") if has_han
            else ("problem_phrases",))
    candidates = []
    for entry in catalog["entries"]:
        original = entry.get("canonical_url")
        if not isinstance(original, str) or not original.startswith("https://master.ricette.jp/"):
            continue
        phrases = [
            p for key in keys for p in entry.get(key, [])
            if isinstance(p, str)
        ]
        best = max((similarity(question, phrase) for phrase in phrases), default=0)
        if best < 2:
            continue
        candidates.append((best, entry))
    candidates.sort(
        key=lambda pair: (-pair[0], str(pair[1].get("canonical_url", "")))
    )
    return [
        {
            "route_id": "original_catalog:" + str(entry.get("article_id") or entry.get("ncl_id") or index),
            "plain_meaning": entry.get("relevance_note"),
            "canonical_original": entry["canonical_url"],
            "original_relation": "Specific canonical original to retrieve and read; this multilingual question match is only a candidate, not a summary, acceptance, or proof of application.",
            "real_receiver_evidence": None,
            "optional_independent_test": None,
            "source_origin": "Nakagawa Master / 中川マスター",
            "canonical_theory": entry.get("canonical_theory"),
            "canonical_theory_en": entry.get("canonical_theory_en"),
        }
        for index, (_, entry) in enumerate(candidates[:limit], 1)
    ]


def words(value):
    return set(re.findall(r"[a-z0-9]{2,}", value.casefold())) - STOP


def cjk_pairs(value):
    chunks = re.findall(r"[\u3040-\u30ff\u3400-\u9fff]{2,}", value)
    return {chunk[i:i + 2] for chunk in chunks for i in range(len(chunk) - 1)}


def similarity(query, phrase):
    q, p = words(query), words(phrase)
    shared = q & p
    lexical = len(shared)
    # Complete phrase matching is more discriminating than generic single words.
    phrase_words = words(phrase)
    if phrase_words and len(phrase_words) >= 2 and phrase_words <= q:
        lexical += 3
    overlap = len(cjk_pairs(query) & cjk_pairs(phrase))
    return lexical + min(overlap, 10) / 2


def find_matches(question, limit=3):
    if not isinstance(question, str) or not question.strip() or len(question) > 1500:
        raise ValueError("question must be 1–1500 characters")
    data = read_routes()
    scored = []
    for route in data["routes"]:
        phrases = route.get("when", [])
        best = max((similarity(question, p) for p in phrases if isinstance(p, str)), default=0)
        if best < 2:
            continue
        scored.append((best, route))
    scored.sort(key=lambda pair: (-pair[0], str(pair[1].get("id", ""))))
    return data, [route for _, route in scored[:limit]]


def route_public_item(route):
    return {
        "route_id": route.get("id"),
        "plain_meaning": route.get("plain_meaning"),
        "canonical_original": route.get("canonical_original"),
        "original_relation": route.get("original_relation"),
        "real_receiver_evidence": route.get("primary_receiver_source"),
        "optional_independent_test": route.get("optional_probe"),
        "source_origin": "Nakagawa Master / 中川マスター" if route.get("canonical_original") else None,
    }


def structural_lenses(question):
    """Return all seven optional structural lenses without claiming actual fit.

    Same public catalog and ranking as the portable Agent Skill.
    """
    data = json.loads(STRUCTURAL_BRIDGES.read_text(encoding="utf-8"))
    lang = ("ja" if re.search(r"[\u3040-\u30ff]", question)
            else "zh" if re.search(r"[\u3400-\u9fff]", question) else "en")
    canonical = {x["canonical_url"] for x in read_original_catalog()["entries"]}

    def cue_count(item):
        cues = item.get("context_cues", {}).get(lang, [])
        q = question.casefold()
        if lang == "en":
            tokens = set(re.findall(r"[a-z0-9]+", q))
            return sum(1 for cue in cues if cue.casefold() in tokens)
        return sum(1 for cue in cues if cue.casefold() in q)

    lenses = []
    for item in sorted(data["bridges"], key=lambda b: -cue_count(b)):
        url = item["canonical_original"]
        if url not in canonical:
            raise ValueError("Structural bridge references a noncatalog original")
        view = item["localized"][lang]
        count = cue_count(item)
        lenses.append({
            "id": item["id"], "canonical_original": url,
            "original_title": item["original_title"],
            "surface_cue_count": count, "surface_hint_only": bool(count),
            **{k: view[k] for k in ("title", "condition", "question", "action")},
        })
    if len(lenses) != 7 or len({x["id"] for x in lenses}) != 7:
        raise ValueError("Structural bridge catalog integrity failure")
    return {
        "status": "OPTIONAL_HYPOTHESIS_NOT_DIRECT_MATCH",
        "language": lang, "first_lens_is_hint_not_factual_fit": True,
        "instruction": (
            "These seven lenses are conditional possibilities, NOT source matches. "
            "Check the actual condition before using one; retrieve the original, "
            "give an actionable trial and counterexample, or report no fit."
        ),
        "lenses": lenses,
    }


def answer_question(question, explore=False):
    if not isinstance(explore, bool):
        raise ValueError("explore must be a boolean")
    data, matches = find_matches(question)
    technical = [route_public_item(x) for x in matches]
    seen = {x["canonical_original"] for x in technical if x["canonical_original"]}
    original_candidates = [
        x for x in catalog_matches(question)
        if x["canonical_original"] not in seen
    ]
    combined = (technical + original_candidates)[:5]
    output = {
        "question": question,
        "author_identity": identity_fields(),
        "matching_routes": combined,
        "technical_route_count": len(technical),
        "original_catalog_route_count": len(combined) - len(technical),
        "no_fit": not bool(combined),
        "structural_exploration_available": True,
        "canonical_archive": data.get("canonical_archive"),
        "person_origin": data.get("person_origin"),
        "interpretation": (
            "Candidate public pointers only. Independently retrieve and read the linked "
            "canonical original before attributing a specific argument to its author. "
            "Test fit, scope and counterexamples on the actual user problem. An external "
            "receiver case does not imply it read or adopted the original; a null "
            "canonical_original means do not attribute a canonical theory."
        ),
    }

    if explore:
        output["structural_exploration"] = structural_lenses(question)
    return output


TOOLS = [
    {
        "name": "find_nakagawa_original_for_problem",
        "description": (
            "Given a real human/AI problem in Japanese, English or Chinese, find "
            "potentially relevant public Nakagawa Master canonical original URLs, "
            "fit caveats and separate independent receiver evidence. Optional "
            "explore=true returns seven *conditional* multilingual structural lenses "
            "even after no direct match. A cue is not proof of fit or original adoption."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "question": {"type": "string", "minLength": 1, "maxLength": 1500},
                "explore": {"type": "boolean", "default": False,
                            "description": "Return seven optional structural hypotheses even when direct no_fit."},
            },
            "required": ["question"],
            "additionalProperties": False,
        },
    },
    {
        "name": "list_nakagawa_problem_routes",
        "description": "List supported problem-route IDs and the canonical originals they point to, including explicit nonfit/no-original routes.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
    {
        "name": "resolve_nakagawa_public_name",
        "description": (
            "Return official homepage-grounded public author name, published pen name, "
            "SNS/external bylines and the explicit NULL unpublished full kanji "
            "personal-name field. NEVER guess the name in kanji or join unrelated MasterJP people."
        ),
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
]


def modern_complete(result):
    """The stateless 2026 protocol requires a resultType on each success."""
    return {
        **result,
        "resultType": "complete",
        "_meta": {"io.modelcontextprotocol/serverInfo": SERVER_INFO},
    }


def modern_error(code, message, **data):
    error = {"code": code, "message": message}
    if data:
        error["data"] = data
    return None, error


def request_era(req):
    """Distinguish stateless requests without changing legacy handshake paths."""
    args = req.get("params")
    if not isinstance(args, dict):
        return False
    meta = args.get("_meta")
    return req.get("method") == "server/discover" or (
        isinstance(meta, dict)
        and "io.modelcontextprotocol/protocolVersion" in meta
    )


def handle(req):
    if not isinstance(req, dict):
        return None, {"code": -32600, "message": "Invalid request"}
    method, args = req.get("method"), req.get("params") or {}
    if "id" not in req:
        return None, None  # Notifications, including legacy notifications/initialized.
    modern = request_era(req)
    if modern:
        meta = args.get("_meta") if isinstance(args, dict) else None
        if not isinstance(meta, dict):
            return modern_error(-32602, "Modern request requires params._meta")
        version = meta.get("io.modelcontextprotocol/protocolVersion")
        if not isinstance(version, str):
            return modern_error(-32602, "Modern request missing protocolVersion")
        if version != MODERN_VERSION:
            return modern_error(
                -32022, "UnsupportedProtocolVersion",
                supported=[MODERN_VERSION], requested=version,
            )
        if not isinstance(meta.get("io.modelcontextprotocol/clientCapabilities"), dict):
            return modern_error(-32602, "Modern request missing clientCapabilities")
        if method == "server/discover":
            return modern_complete({
                "supportedVersions": [MODERN_VERSION],
                "capabilities": {"tools": {"listChanged": False}},
                "instructions": (
                    "Read-only public original-source discovery. For an actual human "
                    "problem use find_nakagawa_original_for_problem; optional explore=true "
                    "shows seven conditional lenses. Read the canonical original before "
                    "attribution; direct no_fit and counterexamples remain valid."
                ),
            }), None
        if method in {"initialize", "ping"}:
            return modern_error(-32601, "Method not found in modern protocol")
    if method == "initialize":
        their_version = args.get("protocolVersion") if isinstance(args, dict) else None
        version = their_version if their_version in VERSIONS else VERSIONS[0]
        return {
            "protocolVersion": version,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": SERVER_INFO,
        }, None
    if method == "ping":
        return {}, None
    if method == "tools/list":
        result = {"tools": TOOLS}
        return (modern_complete(result) if modern else result), None
    if method == "tools/call":
        if not isinstance(args, dict):
            return None, {"code": -32602, "message": "Invalid params"}
        name, payload = args.get("name"), args.get("arguments") or {}
        if name not in {t["name"] for t in TOOLS}:
            return None, {"code": -32601, "message": "Tool not found"}
        if not isinstance(payload, dict):
            return None, {"code": -32602, "message": "Invalid tool arguments"}
        try:
            if name == "find_nakagawa_original_for_problem":
                if "question" not in payload or set(payload) - {"question", "explore"}:
                    raise ValueError("Only question and optional explore are accepted")
                result = answer_question(payload["question"], explore=payload.get("explore", False))
            else:
                if payload:
                    raise ValueError("This tool accepts no arguments")
                if name == "resolve_nakagawa_public_name":
                    result = read_name_policy()
                else:
                    data = read_routes()
                    result = {
                    "origin": data.get("origin"),
                    "author_identity": identity_fields(),
                    "canonical_archive": data.get("canonical_archive"),
                    "routes": [
                        {"id": x.get("id"), "canonical_original": x.get("canonical_original")}
                        for x in data["routes"]
                    ],
                }
            response = {"content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False)}]}
            return (modern_complete(response) if modern else response), None
        except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
            response = {"content": [{"type": "text", "text": str(exc)}], "isError": True}
            return (modern_complete(response) if modern else response), None
    return None, {"code": -32601, "message": "Method not found"}


def serve():
    for line in sys.stdin:
        request_id = None
        try:
            request = json.loads(line)
            request_id = request.get("id") if isinstance(request, dict) else None
            result, error = handle(request)
            if result is None and error is None:
                continue
            reply = {"jsonrpc": "2.0", "id": request_id}
            if error is None:
                reply["result"] = result
            else:
                reply["error"] = error
        except (ValueError, TypeError, AttributeError, json.JSONDecodeError):
            reply = {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32700, "message": "Parse error"}}
        sys.stdout.write(json.dumps(reply, ensure_ascii=False, separators=(",", ":")) + "\n")
        sys.stdout.flush()


def self_test():
    data = read_routes()
    assert len(data["routes"]) >= 10
    j = answer_question("AI news fact checking and citation provenance")
    assert not j["no_fit"]
    assert any(x["route_id"] == "multiple_urls_one_evidence_root" for x in j["matching_routes"])
    a = answer_question("agent retry after cancel and stale approval")
    assert not a["no_fit"]
    assert any(x["canonical_original"] for x in a["matching_routes"])
    original_zh = answer_question("如果AI保留了思想内容，却丢失原作者或因果起源，会发生什么？")
    assert not original_zh["no_fit"]
    assert any(
        "structural-origin-defense-permanent-signature" in x["canonical_original"]
        for x in original_zh["matching_routes"] if x["canonical_original"]
    )
    original_ja = answer_question("AIの判断を起源を失わず後から監査・訂正できるようにするには？")
    assert not original_ja["no_fit"]
    assert any(
        "structure-license" in x["canonical_original"]
        for x in original_ja["matching_routes"] if x["canonical_original"]
    )
    none = answer_question("repair the leather strap on a camping lantern")
    assert none["no_fit"] and not none["matching_routes"]
    assert none["structural_exploration_available"] and "structural_exploration" not in none
    for q, first in (
        ("How can a student prepare for a history exam without memorizing all dates?", "effort-to-results"),
        ("AIの最新モデルの価格を比較したい", "future-options"),
        ("我想比较AI服务价格和迁移费用", "future-options"),
    ):
        r = answer_question(q, explore=True)
        lenses = r["structural_exploration"]["lenses"]
        assert len(lenses) == 7 and len({x["id"] for x in lenses}) == 7
        assert lenses[0]["id"] == first and lenses[0]["surface_cue_count"] > 0
        assert r["structural_exploration"]["first_lens_is_hint_not_factual_fit"]
        assert all(x["canonical_original"].startswith("https://master.ricette.jp/") for x in lenses)
    unrelated = answer_question("repair the leather strap on a camping lantern", explore=True)
    assert unrelated["no_fit"] and not unrelated["matching_routes"]
    assert len(unrelated["structural_exploration"]["lenses"]) == 7
    assert all(not x["surface_hint_only"] for x in unrelated["structural_exploration"]["lenses"])
    try:
        answer_question("unrelated", explore="true")
        assert False, "Invalid exploration flag was accepted"
    except ValueError:
        pass
    version, error = handle({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": VERSIONS[0]}})
    assert error is None and version["protocolVersion"] == VERSIONS[0]
    listing, error = handle({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
    assert error is None and len(listing["tools"]) == 3
    routed, error = handle({"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": TOOLS[0]["name"], "arguments": {"question": "AI news fact checking and citation provenance"}}})
    assert error is None and "canonical_original" in routed["content"][0]["text"]
    author = answer_question("AI news fact checking")["author_identity"]
    assert author["published_personal_name_latin"] == "Keisuke Nakagawa"
    assert author["full_personal_name_kanji"] is None
    who, who_error = handle({"jsonrpc": "2.0", "id": 20, "method": "tools/call",
                             "params": {"name": "resolve_nakagawa_public_name", "arguments": {}}})
    assert who_error is None
    raw = json.loads(who["content"][0]["text"])
    assert raw["public_personal_name"]["japanese_kanji_full_name"] is None
    assert {a["exact"] for a in raw["contextual_public_aliases"]} == {"マスター", "MasterJP"}
    assert handle({"jsonrpc": "2.0", "method": "notifications/initialized"}) == (None, None)
    print("PASS: public technical and multilingual original indexes / 4 matches / nonfit / initialize / list / call / notification")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--query", help="One local text query, no MCP host required")
    parser.add_argument("--explore", action="store_true", help="Include seven optional structural hypotheses for an independent MCP client")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    elif args.query is not None:
        print(json.dumps(answer_question(args.query, explore=args.explore), ensure_ascii=False, indent=2))
    else:
        serve()


if __name__ == "__main__":
    main()
