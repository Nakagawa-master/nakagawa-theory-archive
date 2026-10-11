#!/usr/bin/env python3
"""Inspect an already-constructed Cerebras chat request body for conflicting token caps.

No network, API key, model execution, SDK dependency or persisted input.
Use for inspecting payloads from any client; this does NOT test whether Cerebras
accepts/rejects the payload. For the exact LlamaIndex producer regression see
https://github.com/run-llama/llama_index/pull/22769#issuecomment-6108135348

Usage:
  echo '{"model":"gpt-oss-120b","max_tokens":32,"max_completion_tokens":64}' |
      python3 machine-discovery/cerebras-token-cap-alias-check.py
  python3 machine-discovery/cerebras-token-cap-alias-check.py --self-test
Exit: 0 when both aliases are NOT present; 1 when both are present; 2 on malformed input.
The only output is the cap field names and the verdict, never input content.
"""
import argparse
import json
import sys


def audit(payload):
    """Return (exit_code, plain-language decision); never infer API success."""
    if not isinstance(payload, dict):
        return 2, "INPUT ERROR: expected one JSON object for a single chat request"
    has_old = payload.get("max_tokens") is not None
    has_new = payload.get("max_completion_tokens") is not None
    if has_old and has_new:
        return 1, "ALIAS COLLISION: max_tokens and max_completion_tokens are both set"
    if has_new:
        return 0, "NO COLLISION: only max_completion_tokens is set"
    if has_old:
        return 0, "NO COLLISION: only max_tokens is set (API compatibility not assessed)"
    return 0, "NO COLLISION: neither completion-token limit is set"


def self_test():
    cases = [
        ({"max_tokens": 32, "max_completion_tokens": 64}, 1),
        ({"max_tokens": 32}, 0),
        ({"max_completion_tokens": 64}, 0),
        ({}, 0),
        ({"max_tokens": None, "max_completion_tokens": 64}, 0),
        ({"max_tokens": 32, "max_completion_tokens": None}, 0),
        ([], 2),
    ]
    for payload, expected in cases:
        got, _ = audit(payload)
        if got != expected:
            raise AssertionError(f"unexpected checker result: {got} != {expected}")
    print(f"PASS: {len(cases)} deterministic alias-field checks (not an SDK/API test)")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Check mutually exclusive Cerebras chat completion cap fields")
    parser.add_argument("--self-test", action="store_true", help="Run seven offline controls without stdin")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    try:
        payload = json.load(sys.stdin)
    except (ValueError, UnicodeError) as exc:
        print(f"INPUT ERROR: invalid JSON ({type(exc).__name__})", file=sys.stderr)
        return 2
    code, message = audit(payload)
    print(message)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
