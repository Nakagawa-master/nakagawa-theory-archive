#!/usr/bin/env python3
"""Test the INSTALLED LlamaIndex Redis async_add before any Redis I/O.

All RedisVL index objects are patched before construction. No Redis server,
external network, credentials, or actual index deletion is needed.
Install LlamaIndex's Redis vector-store integration in your own environment,
then run: python3 machine-discovery/redis-async-add-preflight-probe.py

On the reviewed PR head e2ebe01d (2026-10-11), the bad-dims
case is expected to FAIL. The independent PR author then moved validation
ahead of initialization in head ff6136d and added regression tests. The
case SHOULD PASS on that corrected head; this public standalone script
has not been run against its installed dependencies by this archive.
This is a source-order regression, not evidence of real Redis data loss.
"""
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

try:
    from redis.asyncio import Redis as RedisAsync
    from llama_index.core.schema import TextNode
    from llama_index.vector_stores.redis import RedisVectorStore
    from llama_index.vector_stores.redis.schema import (
        RedisVectorStoreSchema, VECTOR_FIELD_NAME,
    )
except ImportError as exc:
    raise SystemExit(
        "Install LlamaIndex's Redis integration and dependencies to run: "
        + str(exc)
    ) from exc


class AsyncAddPreflightTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        schema = RedisVectorStoreSchema()
        schema.fields[VECTOR_FIELD_NAME].attrs.dims = 3
        self.sync_index = MagicMock(schema=schema)
        self.async_index = MagicMock(schema=schema)
        self.async_index.create = AsyncMock()
        self.async_index.load = AsyncMock(return_value=[])

        # Lazy Redis client creation performs no server connection.
        client = RedisAsync.from_url("redis://localhost:6379")
        with (
            patch("llama_index.vector_stores.redis.base.SearchIndex",
                  return_value=self.sync_index),
            patch("llama_index.vector_stores.redis.base.AsyncSearchIndex",
                  return_value=self.async_index),
        ):
            self.store = RedisVectorStore(
                schema=schema, redis_client_async=client, overwrite=True
            )
        self.store.created_async_index = False

    async def test_invalid_embedding_must_not_create_or_drop(self) -> None:
        # Negative control: pre-fix e2ebe01d checked dims after initialization.
        with self.assertRaises(ValueError):
            await self.store.async_add([
                TextNode(text="bad dims", embedding=[0.25])
            ])
        self.async_index.create.assert_not_awaited()
        self.async_index.load.assert_not_awaited()

    async def test_valid_embedding_still_initializes_and_loads(self) -> None:
        await self.store.async_add([
            TextNode(text="valid", embedding=[0.25, -0.5, 1.0])
        ])
        self.async_index.create.assert_awaited_once_with(
            overwrite=True, drop=True
        )
        self.async_index.load.assert_awaited_once()

    async def test_empty_batch_remains_a_noop(self) -> None:
        self.assertEqual(await self.store.async_add([]), [])
        self.async_index.create.assert_not_awaited()
        self.async_index.load.assert_not_awaited()


if __name__ == "__main__":
    unittest.main(verbosity=2)
