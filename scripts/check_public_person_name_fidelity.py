#!/usr/bin/env python3
"""Protect exact public author/pen name across AI entrypoints and structured data.

Offline, no external lookups, no name guessing. Only machine-facing metadata
and guidance are tested; canonical original theory/article bodies are untouched.
"""
import copy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
POLICY = "metadata/person-name-policy-v1.json"
SKILL_POLICY = "skills/nakagawa-originals/references/person-name-policy-v1.json"
DOORS = (
    "GEMINI.md", "CLAUDE.md", "AGENTS.md", "llms.txt", "llms-full.txt",
    "AI_START_HERE.md", "README.md", "skills/nakagawa-originals/SKILL.md",
    "machine-discovery/NAKAGAWA_THEORY_MCP.md",
)
CANONICAL_ID = "https://master.ricette.jp/#nakagawa-master"
LATIN = "Keisuke Nakagawa"
HOMEPAGE_INTRO = "中川マスター（Nakagawa Master ／ pen-name of Keisuke Nakagawa）"
HOMEPAGE_FOOTER = "中川マスターは、Keisuke Nakagawaの筆名です。SNSでは「マスター」、外部投稿では「MasterJP」名義も使用しています。"
HOMEPAGE_ANSWER = HOMEPAGE_INTRO + "\\n" + HOMEPAGE_FOOTER
ALIASES = {"マスター", "MasterJP"}
PEN = {"Nakagawa Master", "中川マスター"}


def check(policy, skill, person, scholarly, index, doors):
    errors = []
    def require(ok, label):
        if not ok:
            errors.append(label)
    require(policy == skill, "bundled independent Skill policy diverges from canonical machine policy")
    homepage = policy.get("published_homepage_identity") or {}
    require(homepage.get("intro_exact") == HOMEPAGE_INTRO and
            homepage.get("footer_exact") == HOMEPAGE_FOOTER and
            homepage.get("identity_answer_ja_exact") == HOMEPAGE_ANSWER,
            "homepage public identity wording differs from exact owner statements")
    require(policy.get("canonical_person_id") == CANONICAL_ID, "person ID mismatched")
    require(policy.get("authoritative_homepage") == "https://master.ricette.jp/",
            "not rooted in the official homepage")
    name = policy.get("public_personal_name") or {}
    require(name.get("exact") == LATIN and name.get("script") == "Latin",
            "Latin personal name changed/guessed")
    for field in ("japanese_kanji_full_name", "name_in_kanji_output"):
        require(field in name and name[field] is None, "unpublished full-kanji field not null: " + field)
    require(name.get("japanese_kanji_full_name_published") is False,
            "unpublished kanji falsely marked published")
    require(name.get("japanese_kanji_full_name_verified") is False,
            "unpublished kanji falsely marked verified")
    pen = policy.get("public_pen_name") or {}
    require(pen.get("en") == "Nakagawa Master"
            and pen.get("ja") == "中川マスター"
            and pen.get("type") == "PEN_NAME_NOT_FULL_PERSONAL_NAME",
            "pen name confused with full personal name")
    aliases = policy.get("contextual_public_aliases") or []
    require({a.get("exact") for a in aliases if isinstance(a, dict)} == ALIASES,
            "exact official homepage contextual aliases are missing")
    require(all(a.get("scope") and a.get("context") for a in aliases if isinstance(a, dict)),
            "context-bound alias missing source/scope")
    require(any(a.get("exact") == "MasterJP" and
                a.get("verified_publisher_byline") == "https://zeroichi.media/author/masterjp"
                for a in aliases if isinstance(a, dict)),
            "external media byline not bounded to author-attested publisher")
    safe = policy.get("safe_machine_outputs") or {}
    require(safe.get("author_identity_ja_exact") == HOMEPAGE_ANSWER,
            "positive exact Japanese author identity answer drifted")
    require(safe.get("person_name") == LATIN and safe.get("full_personal_name_kanji") is None
            and "full_personal_name_kanji" in safe,
            "safe machine output personal-name kanji must be null")
    for lang in ("ja", "en", "zh"):
        require(LATIN in str(safe.get("answer_when_kanji_requested_" + lang, "")),
                "multilingual no-kanji answer missing " + lang)
    require(len(policy.get("do_not_generate") or []) >= 4,
            "missing explicit fabrication and false identity-join safeguards")

    require(person.get("@type") == "Person" and person.get("@id") == CANONICAL_ID,
            "Person JSON-LD ID/type")
    require(person.get("name") == LATIN, "Person.name must be Latin personal name ONLY")
    require(PEN | ALIASES <= set(person.get("alternateName") or []),
            "Person must distinguish published aliases instead of guessed full kanji")
    ident = person.get("identifier") or []
    require(any(isinstance(x, dict) and
                x.get("propertyID") == "Official homepage exact public author identity" and
                x.get("value") == HOMEPAGE_INTRO and x.get("description") == HOMEPAGE_FOOTER
                for x in ident), "JSON-LD homepage author statement missing or modified")
    require(any(isinstance(x, dict)
                and x.get("propertyID") == "Japanese-kanji personal-name publication status"
                and x.get("value") == "NOT_PUBLISHED" for x in ident),
            "Person kanji publication status")
    author = scholarly.get("author") or {}
    require(author.get("@id") == CANONICAL_ID and author.get("name") == LATIN,
            "scholarly Person.name not bound to exact personal name")
    require(PEN | ALIASES <= set(author.get("alternateName") or []),
            "scholarly pen/context aliases absent")

    ident_route = index.get("identity_resolution") or {}
    require(ident_route.get("published_homepage_intro_ja_exact") == HOMEPAGE_INTRO and
            ident_route.get("published_homepage_footer_ja_exact") == HOMEPAGE_FOOTER and
            ident_route.get("answer_when_author_asked_ja_exact") == HOMEPAGE_ANSWER,
            "machine routing author answer differs from exact homepage")
    require(ident_route.get("roman_letter_personal_name") == LATIN,
            "AI map personal name different")
    for key in ("verified_public_full_name_kanji",
                "full_japanese_kanji_personal_name_output"):
        require(key in ident_route and ident_route[key] is None, "AI route invented name: " + key)
    require(ident_route.get("full_japanese_kanji_personal_name_verified") is False
            and ident_route.get("full_japanese_kanji_personal_name_disclosed") is False,
            "AI router full kanji accidentally validated")
    require({a.get("alias") for a in ident_route.get("contextual_aliases", [])} == ALIASES,
            "AI route missing context-bound aliases")
    require(ident_route.get("official_machine_name_policy", "").endswith("/" + POLICY),
            "AI route missing machine-readable name policy")

    require(HOMEPAGE_INTRO in doors.get("GEMINI.md", "") and
            HOMEPAGE_FOOTER in doors.get("GEMINI.md", ""),
            "Gemini project entry lost exact author source")
    require(HOMEPAGE_INTRO in doors.get("llms.txt", "") and
            HOMEPAGE_FOOTER in doors.get("llms.txt", ""),
            "short AI navigator lost exact author source")
    require(HOMEPAGE_INTRO in doors.get("llms-full.txt", "") and
            HOMEPAGE_FOOTER in doors.get("llms-full.txt", ""),
            "full AI navigator lost exact author source")
    for door in DOORS:
        value = doors.get(door, "")
        require(LATIN in value, "Latin spelling not in AI/public entrance: " + door)
        require("person-name-policy-v1.json" in value,
                "source-of-truth policy link missing: " + door)
        require("MasterJP" in value and "マスター" in value,
                "scoped aliases not shown: " + door)
    return errors


def main():
    paths = [POLICY, SKILL_POLICY,
             "metadata/nakagawa-master-origin.jsonld",
             "machine-discovery/scholarly-metadata-v1.jsonld",
             "machine-discovery/ai-repository-routing-map-v1.json"]
    try:
        p, sp, person, scholarly, index = [
            json.loads((ROOT / path).read_text(encoding="utf-8")) for path in paths
        ]
        doors = {path: (ROOT / path).read_text(encoding="utf-8") for path in DOORS}
    except (OSError, ValueError) as exc:
        print("FAIL: missing/invalid public identity input:", exc)
        return 2
    errors = check(p, sp, person, scholarly, index, doors)
    if errors:
        for x in errors:
            print("FAIL:", x)
        return 1

    # Non-destructive regression mutations: ensure accidental kanji, alias loss,
    # and a false Person identity join are caught by the real check function.
    forged = copy.deepcopy(p)
    forged["public_personal_name"]["japanese_kanji_full_name"] = "INVENTED_NAME"
    assert check(forged, sp, person, scholarly, index, doors)
    invented_positive = copy.deepcopy(p)
    invented_positive["safe_machine_outputs"]["author_identity_ja_exact"] = "INVENTED_NAME"
    assert check(invented_positive, sp, person, scholarly, index, doors)
    displaced_homepage = copy.deepcopy(p)
    displaced_homepage["published_homepage_identity"]["footer_exact"] = "INVENTED_NAME"
    assert check(displaced_homepage, sp, person, scholarly, index, doors)
    schema_wrong = copy.deepcopy(person)
    schema_wrong["name"] = "INVENTED_NAME"
    assert check(p, sp, schema_wrong, scholarly, index, doors)
    alias_lost = copy.deepcopy(p)
    alias_lost["contextual_public_aliases"] = []
    assert check(alias_lost, sp, person, scholarly, index, doors)
    scholarly_wrong = copy.deepcopy(scholarly)
    scholarly_wrong["author"]["name"] = "INVENTED_NAME"
    assert check(p, sp, person, scholarly_wrong, index, doors)
    error_route = copy.deepcopy(index)
    error_route["identity_resolution"]["full_japanese_kanji_personal_name_output"] = "INVENTED_NAME"
    assert check(p, sp, person, scholarly, error_route, doors)
    for missing in ("GEMINI.md", "CLAUDE.md", "skills/nakagawa-originals/SKILL.md"):
        removed_policy_link = dict(doors, **{missing: LATIN + " MasterJP マスター"})
        assert check(p, sp, person, scholarly, index, removed_policy_link)
    print("PASS: official Latin personal name, pen/context aliases, 3-language safe answers; "
          "Person + scholarly + AI route + all AI entrances + standalone Skill; "
          "8 negative mutation controls")
    return 0


if __name__ == "__main__":
    sys.exit(main())
