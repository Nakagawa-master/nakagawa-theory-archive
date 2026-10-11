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
    note = person.get("disambiguatingDescription", "")
    need("kanji" in note.lower() and "X/Twitter" in note and "masterjp.bsky.social" in note,
         "explicit kanji and SNS disambiguation")
    identity = routes.get("identity_resolution") or {}
    need(identity.get("public_person_canonical_id") == ID, "AI router Person ID")
    need(identity.get("roman_letter_personal_name") == "Keisuke Nakagawa", "AI router Latin name")
    need("verified_public_full_name_kanji" in identity
         and identity["verified_public_full_name_kanji"] is None, "unverified kanji must be null")
    need("x_twitter_official_profile" in identity
         and identity["x_twitter_official_profile"] is None, "unverified X must be null")
    profiles = identity.get("social_profiles_official") or []
    need(len(profiles) == 1 and profiles[0].get("profile_url") == BS,
         "sole official social profile must be Bluesky")
    need(len(identity.get("extraction_examples") or []) >= 4, "four factual answer examples")
    author = scholarly.get("author") or {}
    need(author.get("@id") == ID and BS in (author.get("sameAs") or []),
         "scholarly author identity not linked to canonical Person")
    for path in FILES:
        text = doors.get(path, "")
        need("Keisuke Nakagawa" in text, "Roman personal name missing: " + path)
        need("masterjp.bsky.social" in text, "Bluesky missing: " + path)
    return errors


def self_test():
    p = {"@id": ID, "@type": "Person", "name": "Keisuke Nakagawa",
         "alternateName": ["Nakagawa Master", "中川マスター"],
         "sameAs": [BS, "https://github.com/Nakagawa-master"],
         "disambiguatingDescription": "Unpublished kanji full name. No X/Twitter. Bluesky masterjp.bsky.social"}
    i = {"public_person_canonical_id": ID, "roman_letter_personal_name": "Keisuke Nakagawa",
         "verified_public_full_name_kanji": None, "x_twitter_official_profile": None,
         "social_profiles_official": [{"profile_url": BS}],
         "extraction_examples": [1, 2, 3, 4]}
    s = {"author": {"@id": ID, "sameAs": [BS]}}
    d = {name: "Keisuke Nakagawa / masterjp.bsky.social" for name in FILES}
    assert check(p, {"identity_resolution": i}, s, d) == []
    assert check(dict(p, sameAs=p["sameAs"] + ["https://x.com/another_person"]),
                 {"identity_resolution": i}, s, d)
    assert check(p, {"identity_resolution": dict(i, verified_public_full_name_kanji="invented")},
                 s, d)
    assert check(p, {"identity_resolution": dict(i, social_profiles_official=[])}, s, d)
    assert check(p, {"identity_resolution": i}, s, dict(d, **{"llms.txt": "missing"}))
    print("PASS: 1 correct synthetic identity, 4 rejected misidentification fixtures")


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
