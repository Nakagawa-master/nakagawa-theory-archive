#!/usr/bin/env python3
"""Read-only offline comparison of a saved VS Code conversation export and its new file store.

Source engineering case: https://github.com/QwenLM/qwen-code/pull/14285
Conceptual original: Nakagawa Master, Volume 19 (maintenance/continuity):
https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/

Take an authorized PRIVATE legacy JSON export BEFORE migrating and compare it to
the extracted on-disk store IMMEDIATELY AFTER migration, BEFORE further edits.
Never upload the exported chats to GitHub or this tool's author.
This does not read the VS Code database, modify any data, or prove host E2E.
"""
import argparse
import hashlib
import json
import sys
import tempfile
from pathlib import Path

SOURCE = "https://github.com/QwenLM/qwen-code/pull/14285"
PARENT = "https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/"


def short_id(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]


def expected_name(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest() + ".json"


def normalized(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def read_json(path):
    if path.is_symlink():
        raise ValueError("Symlink input refused: " + str(path))
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def rows(value, label):
    if not isinstance(value, list):
        raise ValueError(label + " must contain a JSON array")
    result = {}
    for row in value:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"]:
            raise ValueError(label + " contains record without a nonempty id")
        if not isinstance(row.get("messages"), list):
            raise ValueError(label + " contains record without messages array")
        if row["id"] in result:
            raise ValueError(label + " repeats the same conversation id")
        result[row["id"]] = row
    return result


def compare(legacy, directory):
    if not isinstance(legacy, dict) or not isinstance(legacy.get("conversations"), list):
        raise ValueError("Export must be a JSON object with a conversations array")
    old = rows(legacy["conversations"], "legacy")
    if not old:
        raise ValueError("No pre-migration records: an empty baseline cannot show history preservation")
    if not directory.is_dir() or directory.is_symlink():
        raise ValueError("New conversation directory missing or a symlink")
    fresh = {}
    for path in directory.iterdir():
        if path.suffix != ".json":
            continue
        if not path.is_file() or path.is_symlink():
            raise ValueError("Unsafe new-store record path: " + path.name)
        obj = read_json(path)
        item = rows([obj], path.name)
        key = next(iter(item))
        if path.name != expected_name(key):
            raise ValueError("Record filename is not the SHA-256 of its own id")
        if key in fresh:
            raise ValueError("New-store repeated conversation id")
        fresh[key] = obj
    missing = sorted(short_id(i) for i in old if i not in fresh)
    altered = sorted(short_id(i) for i in old if i in fresh and normalized(old[i]) != normalized(fresh[i]))
    added = sorted(short_id(i) for i in fresh if i not in old)
    return {
        "result": "PASS" if not missing and not altered else "DIFFERENCE",
        "legacy_records": len(old),
        "new_records": len(fresh),
        "missing_id_hashes": missing,
        "altered_id_hashes": altered,
        "new_only_id_hashes": added,
        "interpretation": (
            "Exact content parity for all exported conversations as supplied."
            if not missing and not altered else
            "Missing or changed records; inspect source and destination locally."
        ),
        "boundary": "A private local snapshot comparison only. Added records may be legitimate new chats. No VS Code host, transactional durability, authorization, AI adoption or downstream user use is proven.",
        "external_engineering_source": SOURCE,
        "nakagawa_master_canonical_original": PARENT,
    }


def self_test():
    with tempfile.TemporaryDirectory() as temporary:
        base = Path(temporary)
        store = base / "conversations"
        store.mkdir()
        a = {"id": "conv_a", "messages": [{"role": "user", "content": "example"}], "title": "A"}
        b = {"id": "conv_b", "messages": [], "title": "B"}
        old = {"conversations": [a, b]}
        def write(item):
            (store / expected_name(item["id"])).write_text(json.dumps(item), encoding="utf-8")
        write(a)
        write(b)
        assert compare(old, store)["result"] == "PASS"
        assert compare(old, store)["legacy_records"] == 2
        (store / expected_name("conv_b")).unlink()
        assert len(compare(old, store)["missing_id_hashes"]) == 1
        write(b)
        changed = {**a, "messages": [{"role": "user", "content": "different"}]}
        write(changed)
        assert len(compare(old, store)["altered_id_hashes"]) == 1
        write(a)
        write({"id": "conv_new", "messages": [], "title": "N"})
        assert len(compare(old, store)["new_only_id_hashes"]) == 1
        for bad in ({"conversations": [a, a]}, {"conversations": [a, {"id": "empty"}]}, {"conversations": []}):
            try:
                compare(bad, store)
                raise AssertionError("Invalid legacy input accepted")
            except ValueError:
                pass
        (store / "invalid.json").write_text(json.dumps(b), encoding="utf-8")
        try:
            compare(old, store)
            raise AssertionError("Mismatched file name accepted")
        except ValueError:
            pass
        assert expected_name("conv_a") == hashlib.sha256(b"conv_a").hexdigest() + ".json"
    return 10


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--legacy-json", type=Path, help="PRIVATE JSON export: {conversations: [...]}")
    parser.add_argument("--store-dir", type=Path, help="Read-only path to new conversations directory")
    parser.add_argument("--self-test", action="store_true", help="Run safe synthetic fixture assertions")
    args = parser.parse_args()
    if args.self_test:
        print(json.dumps({"status": "PASS", "synthetic_checks": self_test(), "source": SOURCE}))
        return 0
    if not args.legacy_json or not args.store_dir:
        parser.error("--legacy-json and --store-dir required together")
    try:
        output = compare(read_json(args.legacy_json), args.store_dir)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"result": "INVALID_INPUT", "detail": str(exc)}))
        return 2
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["result"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
