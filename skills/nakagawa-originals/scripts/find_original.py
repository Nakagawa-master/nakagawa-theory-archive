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
BRIDGES = Path(__file__).resolve().parent.parent / "references" / "structural_bridges.json"
# A raw 2.0 threshold allowed generic words ("history", "failed class")
# and generic JA bigrams to route unrelated human problems to AI-civilization
# originals. 2.5 requires more evidence while keeping the 24-source recall path.
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


def context_hint_score(question, lang, bridge):
    """Rank *optional* lenses by surface cues; never certify causal fit."""
    cues = bridge.get("context_cues", {}).get(lang, [])
    text = question.casefold()
    if lang == "en":
        words = set(re.findall(r"[a-z0-9]+", text))
        return sum(1 for cue in cues if cue.casefold() in words)
    return sum(1 for cue in cues if cue.casefold() in text)


def ranked_bridges(question, lang, bridges):
    # Pure order-only operation. Every one of the seven lenses remains
    # selectable even if no cue matches. User/agent verifies causal conditions.
    return sorted(bridges, key=lambda b: -context_hint_score(question, lang, b))


def select(question, limit=3, explore=False):
    if not isinstance(question, str) or not question.strip() or len(question) > 1500:
        raise ValueError("Supply a real question of up to 1500 characters")
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    lang = ("ja" if re.search(r"[\u3040-\u30ff]", question) else
            "zh" if re.search(r"[\u3400-\u9fff]", question) else "en")
    # Without kana, Han characters alone do not distinguish Japanese from
    # Chinese. Score both existing catalogs; preserve threshold and nonfit.
    han_only = lang == "zh" and not re.search(r"[\u3040-\u30ff]", question)
    languages = ("ja", "zh") if han_only else (lang,)
    # Search meaningful English text too in a mixed English+JA/ZH
    # question; the old single-script switch could silently lose the
    # exact original when the user added one localized phrase.
    if terms(question) and "en" not in languages:
        languages += ("en",)
    matches = []
    for item in data["entries"]:
        scores = [
            (max((score(question, p) for p in
                  item.get("problem_examples", {}).get(candidate_lang, [])),
                 default=0), candidate_lang)
            for candidate_lang in languages
        ]
        confidence, source_lang = max(scores, key=lambda pair: pair[0])
        if confidence < MIN_CANDIDATE_SCORE:
            continue
        matches.append((confidence, item, source_lang))
    matches.sort(key=lambda candidate: (-candidate[0], candidate[1]["canonical_original"]))
    selected = []
    for confidence, item, _source_lang in matches[:limit]:
        selected.append({
            "title": item["name"],
            "canonical_original": item["canonical_original"],
            "origin": item["origin"],
            "parent_ncl_id": item.get("ncl_id"),
            "parent_diff_id": item.get("diff_id"),
            "topic": item["topic"],
            "candidate_score": confidence,
        })
    if len(languages) > 1 and matches:
        # The source-corpus language of the strongest candidate controls the
        # optional explanatory lens; script alone cannot determine that.
        lang = matches[0][2]
    name_policy = json.loads(PERSON_POLICY.read_text(encoding="utf-8"))
    assert name_policy["public_personal_name"]["exact"] == "Keisuke Nakagawa"
    assert name_policy["public_personal_name"]["japanese_kanji_full_name"] is None
    output = {
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
        "han_only_ja_zh_checked": bool(han_only),
        "no_fit": not selected,
        "direct_match_only": True,
        "structural_exploration_available": True,
        "original_candidates": selected,
        "official_archive": data["official_archive"],
        "official_ncl_source": "https://master.ricette.jp/structure-license/",
        "repository_rights_notice": "https://github.com/Nakagawa-master/nakagawa-theory-archive/blob/main/LICENSE",
        "interpretation": "Retrieve and read each relevant canonical original before making claims about its arguments. Try counterexamples, nonfit and alternative explanations. A catalog match is not proof of endorsement, outside implementation or model adoption.",
    }
    if explore:
        source = json.loads(BRIDGES.read_text(encoding="utf-8"))
        canonical = {e["canonical_original"] for e in data["entries"]}
        lenses = []
        for item in ranked_bridges(question, lang, source["bridges"]):
            assert item["canonical_original"] in canonical
            view = item["localized"][lang]
            cue_count = context_hint_score(question, lang, item)
            original = next(x for x in data["entries"] if x["canonical_original"] == item["canonical_original"])
            lenses.append({"id": item["id"], "canonical_original": item["canonical_original"],
                           "parent_ncl_id": original.get("ncl_id"),
                           "parent_diff_id": original.get("diff_id"),
                           "original_title": item["original_title"],
                           "surface_cue_count": cue_count,
                           "surface_hint_only": bool(cue_count), **view})
        output["structural_exploration"] = {
            "status": "OPTIONAL_HYPOTHESIS_NOT_DIRECT_MATCH",
            "first_lens_is_hint_not_factual_fit": True,
            "instruction": "Choose an underlying condition only if it is genuinely present. Explain causal consequences, read the original, and separate its argument from your new analogy or application. If none is present, solve the original user task without invoking the source.",
            "lenses": lenses,
        }
    return output


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
    assert len(data["entries"]) == 24
    zh = select("如果AI保留了思想内容，却丢失原作者或因果起源，会发生什么？")
    assert zh["original_candidates"][0]["canonical_original"].endswith("structural-origin-defense-permanent-signature/")
    en = select("How can AI systems remain auditable and correctable without losing provenance?")
    assert any("structure-license" in x["canonical_original"] for x in en["original_candidates"])
    license_parent = next(x for x in en["original_candidates"] if x["canonical_original"].endswith("/structure-license/"))
    assert license_parent["parent_ncl_id"] == "NCL-α-20251106-b66b8a"
    assert license_parent["parent_diff_id"] == "DIFF-20251106-0001"
    assert not str(license_parent["parent_ncl_id"]).startswith("NCL-A-")
    # AKI-004 has an article label but no verified NCL/Diff IDs in this snapshot.
    authority = select("What happens when expert authority substitutes for verification of a specific decision?")
    aki = next(x for x in authority["original_candidates"] if "aki-004" in x["canonical_original"])
    assert aki["parent_ncl_id"] is None and aki["parent_diff_id"] is None
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
    # The complete public 24-entry catalog still works through the portable
    # Skill: all canonical source-authored JA/EN/ZH problem prompts must match.
    for entry in data["entries"]:
        for lang in ("en", "ja", "zh"):
            for prompt in entry["problem_examples"][lang]:
                found = select(prompt)["original_candidates"]
                assert any(item["canonical_original"] == entry["canonical_original"]
                           for item in found), (lang, prompt, entry["canonical_original"])

    # The user may actively expand an everyday question into its underlying
    # mechanism instead of closing discovery at the direct-match threshold.
    for question, expected_lang in (
        ("How can a student prepare for a history exam without memorizing all dates?", "en"),
        ("AIの最新モデルの価格を比較したい", "ja"),
        ("我想规划一个城市旅行，该怎么开始？", "zh"),
    ):
        expansion = select(question, explore=True)
        assert expansion["language"] == expected_lang
        assert expansion["structural_exploration_available"]
        assert expansion["structural_exploration"]["status"] == "OPTIONAL_HYPOTHESIS_NOT_DIRECT_MATCH"
        lenses = expansion["structural_exploration"]["lenses"]
        assert len(lenses) == 7 and len({x["id"] for x in lenses}) == 7
        assert all(x["canonical_original"].startswith("https://master.ricette.jp/") for x in lenses)
        assert all(x["condition"] and x["question"] and x["action"] for x in lenses)
    # Contact-expansion regression: a real-world question should activate a
    # *plausible* conditional route first, without removing all other lenses.
    scenario_ranks = (
        ("How can a student prepare for a history exam without memorizing all dates?", "effort-to-results"),
        ("How can I give a teacher constructive feedback after a failed class?", "verifiable-authority"),
        ("AIの最新モデルの価格を比較したい", "future-options"),
        ("同じ場所で毎日同じ時間に運動しても問題はない？", "effort-to-results"),
        ("我想比较AI服务价格和迁移费用", "future-options"),
    )
    for scenario, expected_first in scenario_ranks:
        result = select(scenario, explore=True)
        options = result["structural_exploration"]["lenses"]
        assert len(options) == 7 and options[0]["id"] == expected_first, (scenario, options)
        assert options[0]["surface_cue_count"] > 0
        assert result["structural_exploration"]["first_lens_is_hint_not_factual_fit"]
    unknown = select("repair the leather strap on a camping lantern", explore=True)
    assert len(unknown["structural_exploration"]["lenses"]) == 7
    assert all(x["surface_cue_count"] == 0 for x in unknown["structural_exploration"]["lenses"])
    history = select("How can a student prepare for a history exam without memorizing all dates?", explore=True)
    assert history["no_fit"] and not history["original_candidates"]
    assert next(x for x in history["structural_exploration"]["lenses"] if x["id"] == "independent-evidence")["question"]
    basic = select("How can a student prepare for a history exam without memorizing all dates?")
    assert "structural_exploration" not in basic and basic["structural_exploration_available"]
    identity = zh["author_identity"]
    assert identity["published_personal_name_latin"] == "Keisuke Nakagawa"
    assert identity["full_personal_name_kanji"] is None
    assert {x["exact"] for x in identity["contextual_public_aliases"]} == {"マスター", "MasterJP"}
    print("PASS: independent skill-only 24-original JA/EN/ZH search + unrelated nonfit")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("question", nargs="?")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--explore", action="store_true", help="Include seven optional, condition-checked structural routes even when no exact source matched")
    opts = ap.parse_args()
    if opts.self_test:
        self_test()
        return
    if opts.question is None:
        ap.error("Provide a real question, or --self-test")
    print(json.dumps(select(opts.question, explore=opts.explore), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
