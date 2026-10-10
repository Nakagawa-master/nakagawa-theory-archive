#!/usr/bin/env python3
"""Reproduce numeric EQ/NE precision-boundary differences without LlamaIndex.

Safe default: stdlib-only float64 model (no network, no DB writes).
Optional local mode: QdrantClient(':memory:') with temporary collection.
Optional server mode: requires explicit --server-url AND --allow-server-writes;
creates/deletes only a randomly named collection. Uses QDRANT_API_KEY from the
environment if present; neither key nor endpoint is printed.

This independently tests the Qdrant numeric payload backend, not the
LlamaIndex PR's code, Qdrant server CI, or the Nakagawa theory corpus.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import uuid
from typing import Any

BOUNDARY = 2**53
HIGH = BOUNDARY + 1
PAYLOADS = {
    1: BOUNDARY,
    2: HIGH,
    3: -BOUNDARY,
    4: -HIGH,
    5: 10,
    6: 10.0,
}


def float_model() -> dict[str, Any]:
    """Source-derived precision probe, never presented as a server run."""
    return {
        "backend": "python_stdlib_model_only",
        "performed_qdrant_request": False,
        "positive_ints_distinct": BOUNDARY != HIGH,
        "positive_float64_collision": float(BOUNDARY) == float(HIGH),
        "negative_ints_distinct": -BOUNDARY != -HIGH,
        "negative_float64_collision": float(-BOUNDARY) == float(-HIGH),
        "limitation": "The model predicts collision if a backend converts stored "
        "integers to float64 for range evaluation; it does not prove that a "
        "particular Qdrant version or execution path does so.",
    }


def qdrant_probe(backend: str, server_url: str | None) -> dict[str, Any]:
    """Return actual backend hit IDs for indexed-free temporary payloads."""
    try:
        from qdrant_client import QdrantClient, models
    except ImportError as exc:
        raise RuntimeError(
            "qdrant-client not installed. Install it explicitly in a disposable "
            "Python environment to use local/server mode."
        ) from exc

    if backend == "local":
        client = QdrantClient(":memory:")
    else:
        if not server_url:
            raise ValueError("--server-url is required for server mode")
        # Caller must already have explicitly authorized the remote test writes.
        client = QdrantClient(
            url=server_url, api_key=os.environ.get("QDRANT_API_KEY") or None
        )

    collection = "precision_probe_" + uuid.uuid4().hex[:16]
    created = False
    try:
        client.create_collection(
            collection_name=collection,
            vectors_config=models.VectorParams(
                size=1, distance=models.Distance.DOT
            ),
        )
        created = True
        client.upsert(
            collection_name=collection,
            points=[
                models.PointStruct(
                    id=point_id, vector=[1.0], payload={"n": val}
                )
                for point_id, val in PAYLOADS.items()
            ],
            wait=True,
        )

        def ids(condition: Any, *, negate: bool = False) -> list[int]:
            flt = (
                models.Filter(must_not=[condition])
                if negate
                else models.Filter(must=[condition])
            )
            records, next_offset = client.scroll(
                collection_name=collection,
                scroll_filter=flt,
                limit=100,
                with_payload=False,
                with_vectors=False,
            )
            if next_offset is not None:
                raise RuntimeError("Unexpected pagination for a six-point fixture")
            return sorted(int(p.id) for p in records)

        def range_condition(val: int | float) -> Any:
            # Force the same representable float64 query range bounds in both modes.
            return models.FieldCondition(
                key="n",
                range=models.Range(gte=float(val), lte=float(val)),
            )

        def exact_int(val: int) -> Any:
            return models.FieldCondition(
                key="n", match=models.MatchValue(value=val)
            )

        results: dict[str, Any] = {}
        for label, val in [
            ("positive_lower", BOUNDARY),
            ("negative_lower", -BOUNDARY),
        ]:
            range_c = range_condition(val)
            exact_c = exact_int(val)
            results[label] = {
                "range_eq_ids": ids(range_c),
                "exact_eq_ids": ids(exact_c),
                "range_ne_ids": ids(range_c, negate=True),
                "exact_ne_ids": ids(exact_c, negate=True),
                "desired_exact_eq_ids": [1] if val > 0 else [3],
                "note": "range vs exact is direct Qdrant API behavior, not "
                "an execution of the LlamaIndex PR",
            }
        results["ordinary_cross_type_10"] = {
            "range_eq_ids": ids(range_condition(10)),
            "expected_ids": [5, 6],
        }

        return {
            "backend": backend,
            "performed_qdrant_request": True,
            "temporary_collection_deleted_on_exit": True,
            "collection_has_numeric_payload_index": False,
            "result": results,
            "interpretation": (
                "If a range includes both adjacent large integers but exact "
                "MatchValue picks only the requested one, the inclusive "
                "2**53-range policy lacks separation on this backend. "
                "If not, report the negative result and exact client/server "
                "versions. Local-mode parity does not prove server parity."
            ),
        }
    finally:
        if created:
            client.delete_collection(collection_name=collection)
        client.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--backend", choices=["model", "local", "server"], default="model"
    )
    parser.add_argument(
        "--server-url",
        help="Only for server mode; no endpoint is contacted in model mode",
    )
    parser.add_argument(
        "--allow-server-writes",
        action="store_true",
        help="Explicitly permit temporary collection create/upsert/delete",
    )
    args = parser.parse_args()
    if args.backend == "server" and (
        not args.allow_server_writes or not args.server_url
    ):
        parser.error(
            "server mode requires both --server-url and --allow-server-writes"
        )
    if args.server_url and args.backend != "server":
        parser.error("--server-url is only valid with --backend server")
    if args.allow_server_writes and args.backend != "server":
        parser.error("--allow-server-writes only applies to server mode")
    try:
        result = (
            float_model()
            if args.backend == "model"
            else qdrant_probe(args.backend, args.server_url)
        )
    except Exception as exc:
        # Avoid printing server URLs or credential-bearing exception messages.
        print(
            json.dumps(
                {
                    "backend": args.backend,
                    "status": "unverified_execution_error",
                    "exception_type": type(exc).__name__,
                    "message": (
                        str(exc)
                        if isinstance(exc, (ValueError, RuntimeError))
                        and "not installed" in str(exc)
                        else "Backend probe failed; inspect locally without "
                        "sharing credential-bearing tracebacks."
                    ),
                },
                indent=2,
            ),
            file=sys.stderr,
        )
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
