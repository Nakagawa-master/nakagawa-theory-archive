#!/usr/bin/env python3
"""No-network installed-package check of LlamaIndex legacy image migration.

Upstream bounded receiver evidence:
https://github.com/run-llama/llama_index/pull/23463#issuecomment-6109245470
https://github.com/run-llama/llama_index/pull/23463

Run with the *exact desired* installed llama-index-core version:
    python3 machine-discovery/llamaindex-legacy-images-roundtrip-probe.py

Four independent checks:
 A. an ImageDocument object migrates to one ImageBlock
 B. already-migrated block plus serialized leftover avoids duplicate blocks
 C. resolvable path-backed serialized dict with NO block reconstructs its image
 D. inline-only serialized "husk" with NO block stays intact, rather than
    pretending lost bytes can be recovered from ImageDocument.model_dump()
 E. an unrelated invalid serialized dict is not silently deleted

IMPORTANT: MediaResource.data is excluded from model_dump() by default, so a
plain dump of an inline-only ImageDocument does NOT contain the original image
bytes. The older version of this probe incorrectly expected those absent bytes
to be recovered. D explicitly verifies metadata preservation only.

Exit 0: all five checked input contracts pass on installed package.
Exit 1: an observable contract mismatch.
Exit 2: package missing or a test could not complete.
Only an isolated temporary local PNG is created for C, then deleted.
No network, external API, credential, GitHub write, telemetry, or claim about
real downstream user adoption. No runnable result is claimed until executed.
"""
from __future__ import annotations

import base64
import sys
from pathlib import Path
from tempfile import TemporaryDirectory


def main() -> int:
    try:
        from llama_index.core.base.llms.types import ChatMessage, ImageBlock
        from llama_index.core.schema import ImageDocument
    except ImportError as exc:
        print(f"NOT RUN: install llama-index-core in the test environment ({exc})")
        return 2

    png = (
        b"iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJ"
        b"AAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
    )
    results: list[tuple[str, bool]] = []
    try:
        doc = ImageDocument(image=png)
        expected = doc.resolve_image(as_base64=True).read()

        a_msg = ChatMessage(role="user", additional_kwargs={"images": [doc]})
        a = [block for block in a_msg.blocks if isinstance(block, ImageBlock)]
        results.append(("A object migration -> one image", len(a) == 1 and a[0].image == expected))

        b_msg = ChatMessage.model_validate({
            "role": "user",
            "blocks": [ImageBlock(image=expected).model_dump()],
            "additional_kwargs": {"images": [doc.model_dump()]},
        })
        b = [block for block in b_msg.blocks if isinstance(block, ImageBlock)]
        results.append(("B migrated block + serialized husk -> one image",
                        len(b) == 1 and b[0].image == expected
                        and "images" not in b_msg.additional_kwargs))

        with TemporaryDirectory(prefix="llamaindex-legacy-image-") as tmp:
            img_path = Path(tmp) / "one-pixel.png"
            img_path.write_bytes(base64.b64decode(png))
            c_msg = ChatMessage.model_validate({
                "role": "user",
                "blocks": [],
                "additional_kwargs": {
                    "images": [{"image_resource": {"path": str(img_path)}}]
                },
            })
            c = [block for block in c_msg.blocks if isinstance(block, ImageBlock)]
            results.append(("C serialized path-backed image without block -> recover",
                            len(c) == 1 and c[0].image == expected
                            and "images" not in c_msg.additional_kwargs))

        husk = doc.model_dump()
        d_msg = ChatMessage.model_validate({
            "role": "user", "blocks": [], "additional_kwargs": {"images": [husk]},
        })
        d = [block for block in d_msg.blocks if isinstance(block, ImageBlock)]
        results.append(("D inline-only dump lacking bytes -> preserve husk",
                        len(d) == 0 and d_msg.additional_kwargs.get("images") == [husk]))

        unknown = {"not": "an image document"}
        e_msg = ChatMessage.model_validate({
            "role": "user", "blocks": [], "additional_kwargs": {"images": [unknown]},
        })
        e = [block for block in e_msg.blocks if isinstance(block, ImageBlock)]
        results.append(("E unrecognized dict -> preserve original",
                        len(e) == 0 and e_msg.additional_kwargs.get("images") == [unknown]))
    except Exception as exc:
        print(f"NOT COMPLETED: {type(exc).__name__}: {exc}")
        return 2

    for name, passed in results:
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    if all(passed for _, passed in results):
        print("FIVE CONTRACTS PASS on this installed package; upstream merge/use NOT established")
        return 0
    print("CONTRACT MISMATCH: compare actual installed package against upstream PR #23463")
    return 1


if __name__ == "__main__":
    sys.exit(main())
