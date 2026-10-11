#!/usr/bin/env python3
"""Source-linked, no-network check of legacy image-message migration in LlamaIndex.

Reproduces the input boundary described at:
https://github.com/run-llama/llama_index/pull/23463#issuecomment-6108430896

Run IN a local, authorized environment with llama-index-core installed:
    python3 machine-discovery/llamaindex-legacy-images-roundtrip-probe.py

Reports the current integration's response to three bounded input conditions:
  A: original ImageDocument object, no existing block (must migrate)
  B: serialized document dict AND an already migrated ImageBlock (must not duplicate)
  C: serialized document dict WITHOUT an ImageBlock (must not silently erase)

Exit 0: none of the three input scenarios loses or duplicates an image.
Exit 1: at least one positive/negative condition fails.
Exit 2: package not installed or an exception prevents test completion.
No API calls, credentials, GitHub writes, external files or network I/O.
This check is not evidence a public maintainer adopted the fix or that an end
user actually lost an image in a deployed application.
"""
from __future__ import annotations

import sys


def main() -> int:
    try:
        from llama_index.core.base.llms.types import ChatMessage, ImageBlock
        from llama_index.core.schema import ImageDocument
    except ImportError as exc:
        print(f"NOT RUN: install llama-index-core in the test environment ({exc})")
        return 2

    # Minimal, public one-pixel PNG test fixture from upstream's own tests.
    png = (b"iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJ"
           b"AAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")
    try:
        doc = ImageDocument(image=png)
        expected = doc.resolve_image(as_base64=True).read()

        object_only = ChatMessage(
            role="user", additional_kwargs={"images": [doc]}
        )
        a = [b for b in object_only.blocks if isinstance(b, ImageBlock)]
        a_pass = len(a) == 1 and a[0].image == expected

        already_migrated = ChatMessage.model_validate({
            "role": "user",
            "blocks": [ImageBlock(image=expected).model_dump()],
            "additional_kwargs": {"images": [doc.model_dump()]},
        })
        b = [v for v in already_migrated.blocks if isinstance(v, ImageBlock)]
        b_pass = len(b) == 1 and b[0].image == expected

        dict_only = ChatMessage.model_validate({
            "role": "user",
            "blocks": [],
            "additional_kwargs": {"images": [doc.model_dump()]},
        })
        c = [v for v in dict_only.blocks if isinstance(v, ImageBlock)]
        # Supporting this import is one policy option. Alternatively, an
        # unsupported dict-only source should fail explicitly rather than
        # successful validation followed by loss of both image representations.
        c_pass = len(c) == 1 and c[0].image == expected
    except Exception as exc:
        print(f"NOT COMPLETED: {type(exc).__name__}: {exc}")
        return 2

    print("A ImageDocument object -> one block:", "PASS" if a_pass else "FAIL")
    print("B dict plus existing block -> exactly one:", "PASS" if b_pass else "FAIL")
    print("C dict without existing block -> one image:", "PASS" if c_pass else "FAIL (silent-loss candidate)")
    if all((a_pass, b_pass, c_pass)):
        print("ALL THREE PASS; verify application-level round-trip separately")
        return 0
    print("FAIL: see LlamaIndex PR #23463 for producer context; no live data-loss claim")
    return 1


if __name__ == "__main__":
    sys.exit(main())
