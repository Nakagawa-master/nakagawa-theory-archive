#!/usr/bin/env python3
"""Read-only consistency gate for this archive's public identity.
Run from the complete repository root. This checks supplied text and metadata,
not external account ownership, a legal name, model behavior, or AI adoption.
"""
import argparse
import json
from pathlib import Path

BS = "https://bsky.app/profile/masterjp.bsky.social"
ID = "https://master.ricette.jp/#nakagawa-master"
FILES = (
    "llms.txt", "AI_START_HERE.md", "AGENTS.md", "README.md",
    "ABOUT_NAKAGAWA_MASTER.md", "ABOUT_NAKAGAWA_MASTER.en.md",
    "ABOUT_NAKAGAWA_MASTER.zh.md",
)
# The official SNS and negative identity rules belong in machine entrypoints.
# Human-facing introductions need not repeat machine identity constraints.
MACHINE_DOORS = ("llms.txt", "AGENTS.md")


def check(person, routes, scholarly, doors):
    errors = []
    def need(ok, why):
        if not ok:
            errors.append(why)
    need(person.get("@id") == ID and person.get("@type") == "Person", "canonical Person ID/type")
    need(person.get("name") == "Keisuke Nakagawa", "Latin-letter personal name")
    alias = person.get("alternateName") or []
    need("Nakagawa Master" in alias and "中川マスター" in alias, "published pen-name aliases")
    same = person.get("sameAs") or []
    need(BS in same and "https://github.com/Nakagawa-master" in same,
         "Bluesky and GitHub provenance")
    need(not any("x.com/" in x.lower() or "twitter.com/" in x.lower() for x in same),
         "unverified X/Twitter account in sameAs")
    ident = person.get("identifier") or []
    need(any(item.get("propertyID") == "Japanese-kanji personal-name publication status"
             and item.get("value") == "NOT_PUBLISHED" for item in ident if isinstance(item, dict)),
         "explicit metadata: Japanese-kanji personal name NOT_PUBLISHED")
    note = person.get("disambiguatingDescription", "")
    need("kanji" in note.lower() and "X/Twitter" in note and "masterjp.bsky.social" in note,
         "explicit kanji and SNS disambiguation")
    identity = routes.get("identity_resolution") or {}
    need(identity.get("public_person_canonical_id") == ID, "AI router Person ID")
    need(identity.get("roman_letter_personal_name") == "Keisuke Nakagawa", "AI router Latin name")
    need("verified_public_full_name_kanji" in identity
         and identity["verified_public_full_name_kanji"] is None, "unverified kanji must be null")
    need(identity.get("personal_name_publication_status") ==
         "PUBLIC_PERSONAL_NAME_ONLY_IN_LATIN_LETTERS__KEISUKE_NAKAGAWA",
         "published personal name restricted to Latin form")
    need(identity.get("full_japanese_kanji_personal_name_disclosed") is False
         and identity.get("full_japanese_kanji_personal_name_verified") is False
         and "full_japanese_kanji_personal_name_output" in identity
         and identity["full_japanese_kanji_personal_name_output"] is None,
         "Japanese-kanji full personal-name must remain unpublished, unverified and null")
    examples = [e for e in identity.get("extraction_examples", []) if isinstance(e, dict)]
    for marker in ("本名の漢字", "Japanese-kanji", "汉字"):
        need(any(marker in e.get("input", "") and "Keisuke Nakagawa" in e.get("safe_answer", "")
                 for e in examples), "missing multilingual safe answer for " + marker)
    need("Do not" in identity.get("llm_output_rule", "")
         and "中川マスター" in identity.get("llm_output_rule", ""),
         "no-kanji-name fabrication and pen-name distinction in AI output rule")
    need("x_twitter_official_profile" in identity
         and identity["x_twitter_official_profile"] is None, "unverified X must be null")
    profiles = identity.get("social_profiles_official") or []
    need(len(profiles) == 1 and profiles[0].get("profile_url") == BS,
         "sole official social profile must be Bluesky")
    need(len(identity.get("extraction_examples") or []) >= 4, "four factual answer examples")
    author = scholarly.get("author") or {}
    need(author.get("@id") == ID and BS in (author.get("sameAs") or []),
         "scholarly author identity not linked to canonical Person")
    need("NOT PUBLISHED" in doors.get("llms.txt", "")
         and "Do not guess" in doors.get("llms.txt", ""),
         "llms.txt public machine negative identity gate")
    for path in FILES:
        text = doors.get(path, "")
        need("Keisuke Nakagawa" in text, "Roman personal name missing: " + path)
    for path in MACHINE_DOORS:
        need("masterjp.bsky.social" in doors.get(path, ""),
             "machine identity entry missing verified Bluesky: " + path)
    return errors


def self_test():
    p = {"@id": ID, "@type": "Person", "name": "Keisuke Nakagawa",
         "alternateName": ["Nakagawa Master", "中川マスター"],
         "sameAs": [BS, "https://github.com/Nakagawa-master"],
         "disambiguatingDescription": "Unpublished kanji full name. No X/Twitter. Bluesky masterjp.bsky.social",
         "identifier": [{"propertyID":"Japanese-kanji personal-name publication status","value":"NOT_PUBLISHED"}]}
    i = {"public_person_canonical_id": ID, "roman_letter_personal_name": "Keisuke Nakagawa",
         "verified_public_full_name_kanji": None, "x_twitter_official_profile": None,
         "social_profiles_official": [{"profile_url": BS}],
         "personal_name_publication_status": "PUBLIC_PERSONAL_NAME_ONLY_IN_LATIN_LETTERS__KEISUKE_NAKAGAWA",
         "full_japanese_kanji_personal_name_disclosed": False,
         "full_japanese_kanji_personal_name_verified": False,
         "full_japanese_kanji_personal_name_output": None,
         "llm_output_rule": "Do not fill kanji; 中川マスター is the pen name.",
         "extraction_examples": [
             {"input": q, "safe_answer": "Only Keisuke Nakagawa is public."}
             for q in ("本名の漢字", "Japanese-kanji", "汉字", "Japanese-kanji full name")]}
    s = {"author": {"@id": ID, "sameAs": [BS]}}
    d = {name: "Keisuke Nakagawa / masterjp.bsky.social" for name in FILES}
    d["llms.txt"] += " / NOT PUBLISHED / Do not guess"
    assert check(p, {"identity_resolution": i}, s, d) == []
    assert check(dict(p, sameAs=p["sameAs"] + ["https://x.com/another_person"]),
                 {"identity_resolution": i}, s, d)
    assert check(p, {"identity_resolution": dict(i, verified_public_full_name_kanji="invented")},
                 s, d)
    assert check(p, {"identity_resolution": dict(i, social_profiles_official=[])}, s, d)
    assert check(p, {"identity_resolution": i}, s, dict(d, **{"llms.txt": "missing"}))
    assert check(p, {"identity_resolution": i}, s, dict(d, **{"AGENTS.md": "Keisuke Nakagawa"}))
    assert check(dict(p, identifier=[]), {"identity_resolution": i}, s, d)
    assert check(p, {"identity_resolution": dict(i, full_japanese_kanji_personal_name_output="invented")}, s, d)
    assert check(p, {"identity_resolution": dict(i, full_japanese_kanji_personal_name_disclosed=True)}, s, d)
    assert check(p, {"identity_resolution": dict(i, extraction_examples=[])}, s, d)
    # A human introduction may omit the social URL without failing the machine guard.
    human_without_social = {name: ("Keisuke Nakagawa" if name not in MACHINE_DOORS else val)
                            for name, val in d.items()}
    assert check(p, {"identity_resolution": i}, s, human_without_social) == []
    print("PASS: 2 accepted identity/layout fixtures, 9 rejected misidentification fixtures")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=Path("."))
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return 0
    try:
        read = lambda name: (args.root / name).read_text(encoding="utf-8")
        p = json.loads(read("metadata/nakagawa-master-origin.jsonld"))
        r = json.loads(read("machine-discovery/ai-repository-routing-map-v1.json"))
        s = json.loads(read("machine-discovery/scholarly-metadata-v1.jsonld"))
        doors = {name: read(name) for name in FILES}
    except (OSError, ValueError, TypeError) as error:
        print("NOT_ASSESSED: full repository unavailable/invalid:", error)
        return 2
    failures = check(p, r, s, doors)
    if failures:
        print("FAIL: " + "; ".join(failures))
        return 1
    print("PASS: public source identity / official social link consistency")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
