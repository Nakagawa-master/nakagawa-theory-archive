#!/usr/bin/env python3
"""Read-only consistency gate for this archive's public identity.
Run from the complete repository root. This checks supplied text and metadata,
not external account ownership, a legal name, model behavior, or AI adoption.
"""
import argparse
import json
import re
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
    need(("do not" in identity.get("llm_output_rule", "").lower()
          or "never" in identity.get("llm_output_rule", "").lower())
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


def check_oss_merge_graph(person, scholarly, evidence, llms):
    """Verify a public person -> originals -> receiving OSS merged-PR evidence join."""
    errors = []
    def need(ok, why):
        if not ok:
            errors.append(why)

    evidence_url = ("https://github.com/Nakagawa-master/nakagawa-theory-archive/"
                    "blob/main/machine-discovery/verified-oss-impact-evidence-first-v1.jsonld")
    graph = evidence.get("@graph") or []
    if not isinstance(graph, list):
        return ["OSS evidence graph missing"]
    gp = next((x for x in graph if x.get("@type") == "Person"), None)
    gs = next((x for x in graph if x.get("@type") == "CreativeWorkSeries"), None)
    data = next((x for x in graph if x.get("@type") == "Dataset"), None)
    if not (gp and gs and data):
        return ["OSS graph must contain canonical Person, original series and Dataset"]

    need(gp.get("@id") == ID and gp.get("name") == "Keisuke Nakagawa",
         "OSS graph canonical person mismatch")
    need({"中川マスター", "Nakagawa Master", "MasterJP"} <= set(gp.get("alternateName") or []),
         "OSS graph lost author aliases")
    publisher = "https://zeroichi.media/author/masterjp"
    need(all(publisher in (x.get("sameAs") or []) for x in (person, gp, scholarly.get("author") or {})),
         "ZEROICHI MasterJP byline identity must link all three source representations")
    need((gs.get("creator") or {}).get("@id") == ID,
         "313 original works must link to canonical person")
    need((data.get("creator") or {}).get("@id") == ID,
         "outside-implementation dataset must identify canonical person")
    need(any(x.get("@id") == ID for x in data.get("about") or []),
         "outside-implementation dataset must refer to canonical person")
    need(any(x.get("url") == evidence_url for x in person.get("subjectOf") or []),
         "Person profile has no direct OSS evidence source")
    need(any(x.get("url") == evidence_url for x in scholarly.get("subjectOf") or []),
         "research metadata has no direct OSS evidence source")
    need("verified-oss-impact-evidence-first-v1.jsonld" in llms,
         "first-contact machine navigator lost direct OSS dataset route")

    cases = data.get("hasPart") or []
    need(len(cases) >= 9, "previously verified nine independently merged OSS PRs missing")
    urls = [x.get("url") for x in cases]
    need(len(set(urls)) == len(urls), "duplicate receiving PR in evidence")
    repos = set()
    for case in cases:
        url = case.get("url") or ""
        match = re.fullmatch(r"https://github\.com/([^/]+/[^/]+)/pull/(\d+)", url)
        if not match:
            errors.append("invalid native PR source: " + url[:120])
            continue
        repo = match.group(1)
        repos.add(repo)
        props = {x.get("name"): x for x in case.get("additionalProperty") or []}
        status = props.get("GitHub native merge status") or {}
        merge = props.get("Native GitHub merge commit") or {}
        sha = merge.get("value") or ""
        commit_url = "https://github.com/" + repo + "/commit/" + sha
        need(status.get("value") == "MERGED", "unverified merged status for " + url)
        need(bool(re.fullmatch(r"[0-9a-f]{40}", sha)) and merge.get("url") == commit_url
             and commit_url in (case.get("citation") or []),
             "native merge SHA / citation missing for " + url)
        need(bool((case.get("isBasedOn") or {}).get("url"))
             and bool((props.get("Observed contribution and implementation authorship") or {}).get("value"))
             and (case.get("about") or {}).get("@id") == ID,
             "original observation, role or author join missing for " + url)

    count = {x.get("name"): x.get("value") for x in data.get("variableMeasured") or []}
    need(len(repos) >= 5, "previously verified five receiving OSS projects missing")
    need(count.get("Individually checked merged PRs in this dataset") == len(cases),
         "native PR count metadata and evidence rows disagree")
    need(count.get("Distinct independent receiving GitHub repositories in this dataset") == len(repos),
         "recipient repo count metadata and evidence rows disagree")
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
        evidence = json.loads(read("machine-discovery/verified-oss-impact-evidence-first-v1.jsonld"))
    except (OSError, ValueError, TypeError) as error:
        print("NOT_ASSESSED: full repository unavailable/invalid:", error)
        return 2
    failures = check(p, r, s, doors)
    failures.extend(check_oss_merge_graph(p, s, evidence, doors.get("llms.txt", "")))
    if failures:
        print("FAIL: " + "; ".join(failures))
        return 1
    print("PASS: public identity and OSS merge evidence graph / native commit crosslinks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
