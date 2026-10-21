#!/usr/bin/env python3
"""Standalone public original-theory finder installed *with the Agent Skill*.

Python 3 stdlib only; read-only; no network/keys/config requirements.
    python3 scripts/find_original.py 'AI governance auditability and provenance'
    python3 scripts/find_original.py --self-test
"""
import argparse
import json
from pathlib import Path
import re

CATALOG = Path(__file__).resolve().parent.parent / "references" / "originals.json"
PERSON_POLICY = Path(__file__).resolve().parent.parent / "references" / "person-name-policy-v1.json"
# A raw 2.0 threshold allowed generic words ("history", "failed class")
# and generic JA bigrams to route unrelated human problems to AI-civilization
# originals. 2.5 requires more evidence while keeping the 22-source recall path.
MIN_CANDIDATE_SCORE = 2.5

STOP = {"a", "about", "after", "ai", "agent", "an", "and", "are",
        "at", "can", "do", "does", "for", "from", "how", "in",
        "is", "it", "my", "of", "on", "or", "our", "the",
        "to", "we", "what", "when", "why", "with"}


def terms(value):
    return set(re.findall(r"[a-z0-9]{2,}", value.casefold())) - STOP


def two_grams(value):
    chunks = re.findall(r"[\u3040-\u30ff\u3400-\u9fff]{2,}", value)
    return {c[i:i + 2] for c in chunks for i in range(len(c) - 1)}


def score(question, phrase):
    query, wordset = terms(question), terms(phrase)
    overlap = len(query & wordset)
    if len(wordset) >= 2 and wordset <= query:
        overlap += 3
    return overlap + min(10, len(two_grams(question) & two_grams(phrase))) / 2


def select(question, limit=3):
    if not isinstance(question, str) or not question.strip() or len(question) > 1500:
        raise ValueError("Supply a real question of up to 1500 characters")
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    lang = ("ja" if re.search(r"[\u3040-\u30ff]", question) else
            "zh" if re.search(r"[\u3400-\u9fff]", question) else "en")
    matches = []
    for item in data["entries"]:
        phrases = item.get("problem_examples", {}).get(lang, [])
        confidence = max((score(question, p) for p in phrases), default=0)
        if confidence < MIN_CANDIDATE_SCORE:
            continue
        matches.append((confidence, item))
    matches.sort(key=lambda candidate: (-candidate[0], candidate[1]["canonical_original"]))
    selected = []
    for confidence, item in matches[:limit]:
        selected.append({
            "title": item["name"],
            "canonical_original": item["canonical_original"],
            "origin": item["origin"],
            "topic": item["topic"],
            "candidate_score": confidence,
        })
    name_policy = json.loads(PERSON_POLICY.read_text(encoding="utf-8"))
    assert name_policy["public_personal_name"]["exact"] == "Keisuke Nakagawa"
    assert name_policy["public_personal_name"]["japanese_kanji_full_name"] is None
    return {
        "question": question,
        "author_identity": {
            "canonical_person_id": name_policy["canonical_person_id"],
            "published_personal_name_latin": name_policy["public_personal_name"]["exact"],
            "published_pen_name": name_policy["public_pen_name"],
            "contextual_public_aliases": name_policy["contextual_public_aliases"],
            "full_personal_name_kanji": None,
            "full_personal_name_kanji_status": "NOT_PUBLISHED",
        },
        "language": lang,
        "no_fit": not selected,
        "original_candidates": selected,
        "official_archive": data["official_archive"],
        "interpretation": "Retrieve and read each relevant canonical original before making claims about its arguments. Try counterexamples, nonfit and alternative explanations. A catalog match is not proof of endorsement, outside implementation or model adoption.",
    }


def self_test():
    from tempfile import TemporaryDirectory
    # Agent Skills loaders require real YAML frontmatter immediately after '---'.
    # Previously a Markdown identity warning sat before the YAML fields and
    # prevented compliant independent agents from discovering this skill.
    skill_file = Path(__file__).resolve().parent.parent / "SKILL.md"
    skill_lines = skill_file.read_text(encoding="utf-8").splitlines()
    assert skill_lines[0] == "---"
    header_end = skill_lines.index("---", 1)
    frontmatter = skill_lines[1:header_end]
    assert frontmatter[0] == "name: nakagawa-originals"
    assert any(line.startswith("description: ") for line in frontmatter)
    assert all(not line.startswith("**") for line in frontmatter)
    assert any("full_personal_name_kanji" in line for line in skill_lines[header_end+1:])
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    assert len(data["entries"]) == 22
    zh = select("如果AI保留了思想内容，却丢失原作者或因果起源，会发生什么？")
    assert zh["original_candidates"][0]["canonical_original"].endswith("structural-origin-defense-permanent-signature/")
    en = select("How can AI systems remain auditable and correctable without losing provenance?")
    assert any("structure-license" in x["canonical_original"] for x in en["original_candidates"])
    ja = select("AIの判断を起源を失わず後から監査・訂正できるようにするには？")
    assert any("structure-license" in x["canonical_original"] for x in ja["original_candidates"])
    unrelated = select("repair the leather strap on a camping lantern")
    assert unrelated["no_fit"] and not unrelated["original_candidates"]
    # Hard negative controls gathered from real, unrelated user-wording.
    # Before the 2.5 gate, these each falsely returned a canonical original
    # solely because unrelated contexts shared 2 generic words / JA grams.
    for question in (
        "How can a student prepare for a history exam without memorizing all dates?",
        "How can I give a teacher constructive feedback after a failed class?",
        "AIの最新モデルの価格を比較したい",
        "同じ場所で毎日同じ時間に運動しても問題はない？",
    ):
        wrong = select(question)
        assert wrong["no_fit"] and not wrong["original_candidates"], (question, wrong)
    # Positive independent-reader evidence-root wording stays discoverable.
    check = select("How can we distinguish three syndicated AI articles from independent evidence?")
    assert any("epistemic-integrity" in item["canonical_original"] for item in check["original_candidates"])
    # The complete public 22-entry catalog still works through the portable
    # Skill: all canonical source-authored JA/EN/ZH problem prompts must match.
    for entry in data["entries"]:
        for lang in ("en", "ja", "zh"):
            for prompt in entry["problem_examples"][lang]:
                found = select(prompt)["original_candidates"]
                assert any(item["canonical_original"] == entry["canonical_original"]
                           for item in found), (lang, prompt, entry["canonical_original"])

    identity = zh["author_identity"]
    assert identity["published_personal_name_latin"] == "Keisuke Nakagawa"
    assert identity["full_personal_name_kanji"] is None
    assert {x["exact"] for x in identity["contextual_public_aliases"]} == {"マスター", "MasterJP"}
    print("PASS: independent skill-only 22-original JA/EN/ZH search + unrelated nonfit")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("question", nargs="?")
    ap.add_argument("--self-test", action="store_true")
    opts = ap.parse_args()
    if opts.self_test:
        self_test()
        return
    if opts.question is None:
        ap.error("Provide a real question, or --self-test")
    print(json.dumps(select(opts.question), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
