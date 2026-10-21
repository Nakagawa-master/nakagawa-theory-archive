#!/usr/bin/env python3
"""Regression for exact public author identity, separate from theory evaluation.

Source: https://master.ricette.jp/
Only the pen name 中川マスター / Nakagawa Master and the personal-name Latin
spelling Keisuke Nakagawa are published. A Japanese-kanji full personal name
must remain NULL, and similar-name search hits are not same-person evidence.
"""
import json
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parent.parent
IDENTITY = REPO / "metadata" / "nakagawa-master-name-identity.json"
PERSON = REPO / "metadata" / "nakagawa-master-origin.jsonld"
ROUTES = REPO / "machine-discovery" / "ai-repository-routing-map-v1.json"
EXPECTED_ID = "https://master.ricette.jp/#nakagawa-master"
EXPECTED_ROMAN = "Keisuke Nakagawa"
EXPECTED_PEN_JA = "中川マスター"
EXPECTED_PEN_EN = "Nakagawa Master"


def validate(policy, person, routes):
    errors = []
    if policy.get("@id") != EXPECTED_ID:
        errors.append("Canonical person ID changed")
    if policy.get("canonical_official_site") != "https://master.ricette.jp/":
        errors.append("Official source changed")
    for key, value in (
        ("official_display_name_ja", EXPECTED_PEN_JA),
        ("official_display_name_en", EXPECTED_PEN_EN),
        ("person_name_latin", EXPECTED_ROMAN),
        ("kanji_full_name_publication_status", "NOT_PUBLISHED"),
    ):
        if policy.get(key) != value:
            errors.append("Identity field mismatch: " + key)
    if "official_public_personal_full_name_kanji" not in policy or policy["official_public_personal_full_name_kanji"] is not None:
        errors.append("Unpublished kanji name must be explicitly null")
    flag = policy.get("author_name_surface_policy", {})
    for key in (
        "no_kanji_completion",
        "do_not_transliterate_roman_letters_to_kanji",
        "do_not_predict_given_name_kanji",
        "do_not_mislabel_pen_name_as_kanji_full_name",
        "do_not_join_another_person_from_shared_reading",
        "not_published_is_not_a_missing_value_to_fill",
    ):
        if flag.get(key) is not True:
            errors.append("Machine identity prohibition absent: " + key)
    if flag.get("allowed_official_display_forms") != [
        EXPECTED_PEN_JA, EXPECTED_PEN_EN, EXPECTED_ROMAN
    ]:
        errors.append("Unverified display forms were added")
    if person.get("@type") != "Person" or person.get("@id") != EXPECTED_ID:
        errors.append("Person JSON-LD does not match the canonical person")
    if person.get("name") != EXPECTED_ROMAN:
        errors.append("JSON-LD Person.name is not the exact published Latin name")
    if person.get("alternateName") != [EXPECTED_PEN_EN, EXPECTED_PEN_JA]:
        errors.append("JSON-LD contains unverified alternate names")
    if not any(
        entry.get("propertyID") == "Japanese-kanji personal-name publication status"
        and entry.get("value") == "NOT_PUBLISHED"
        for entry in person.get("identifier", [])
    ):
        errors.append("JSON-LD lacks NOT_PUBLISHED kanji status")
    map_identity = routes.get("identity_resolution", {})
    for key, val in (
        ("public_person_canonical_id", EXPECTED_ID),
        ("author_pen_name_english", EXPECTED_PEN_EN),
        ("author_pen_name_japanese", EXPECTED_PEN_JA),
        ("roman_letter_personal_name", EXPECTED_ROMAN),
    ):
        if map_identity.get(key) != val:
            errors.append("AI routing map identity drift: " + key)
    if "verified_public_full_name_kanji" not in map_identity or map_identity["verified_public_full_name_kanji"] is not None:
        errors.append("AI routing map must keep unpublished kanji explicitly null")
    return errors


def self_test(policy, person, routes):
    assert not validate(policy, person, routes)
    mutant = json.loads(json.dumps(policy))
    mutant["official_public_personal_full_name_kanji"] = "invented-name-not-a-real-person"
    assert any("explicitly null" in x for x in validate(mutant, person, routes))
    mutant = json.loads(json.dumps(policy))
    mutant["author_name_surface_policy"]["do_not_predict_given_name_kanji"] = False
    assert any("prohibition absent" in x for x in validate(mutant, person, routes))
    mutant = json.loads(json.dumps(person))
    mutant["name"] = "unverified-identity"
    assert any("exact published" in x for x in validate(policy, mutant, routes))


def main():
    policy = json.loads(IDENTITY.read_text(encoding="utf-8"))
    person = json.loads(PERSON.read_text(encoding="utf-8"))
    routes = json.loads(ROUTES.read_text(encoding="utf-8"))
    self_test(policy, person, routes)
    errors = validate(policy, person, routes)
    for filename in ("GEMINI.md", "AGENTS.md", "CLAUDE.md", "llms.txt"):
        text = (REPO / filename).read_text(encoding="utf-8")
        if "metadata/nakagawa-master-name-identity.json" not in text:
            errors.append("Machine identity policy link missing in " + filename)
    if errors:
        for err in errors:
            print("PUBLIC_IDENTITY_ERROR: " + err, file=sys.stderr)
        return 1
    print("PASS: official author Latin/pen-name exact; kanji full name null; cross-index equality; negative mutations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
