#!/usr/bin/env python3
"""A runnable model of an uncertain approval-resume delivery boundary.

Run: python3 approval-delivery-ack-lab.py

This is an independent standard-library educational simulation, NOT Mastra or
Inngest source, NOT a test of a deployed package, and NOT evidence that an actual
customer's approved effect ran twice. It illustrates a failure class independently
reviewed in mastra-ai/mastra PR #29451 (lost acknowledgement after event acceptance).
"""
from __future__ import annotations

import unittest
from dataclasses import dataclass


class MissingAck(Exception):
    """The client cannot establish whether the event was accepted."""


@dataclass(frozen=True)
class Resume:
    suspension: str
    effect: str
    event_id: str | None = None


class FakeQueue:
    """One process models acceptance, deduplication, and the observable effect."""

    def __init__(self) -> None:
        self.seen_ids: set[str] = set()
        self.effects: list[tuple[str, str]] = []
        self.deliveries = 0

    def send(self, event: Resume, *, outcome: str = "ack") -> None:
        if outcome not in {"ack", "accept_then_lose_ack", "reject_before_accept"}:
            raise ValueError(outcome)
        if outcome == "reject_before_accept":
            raise MissingAck("transport rejected before queue acceptance")

        self.deliveries += 1
        if event.event_id is None or event.event_id not in self.seen_ids:
            if event.event_id is not None:
                self.seen_ids.add(event.event_id)
            self.effects.append((event.suspension, event.effect))

        if outcome == "accept_then_lose_ack":
            raise MissingAck("the queue accepted the event, but its ack was lost")


def retry_after_uncertain_delivery(queue: FakeQueue, event: Resume, *, first: str) -> None:
    """A sender retries once; it does not assume a timeout means nonacceptance."""
    try:
        queue.send(event, outcome=first)
    except MissingAck:
        queue.send(event)


class DeliveryBoundaryTests(unittest.TestCase):
    def test_unkeyed_retry_can_execute_one_approval_twice(self) -> None:
        queue = FakeQueue()
        retry_after_uncertain_delivery(
            queue, Resume("paused-run-A", "approved-tool"), first="accept_then_lose_ack"
        )
        self.assertEqual(queue.effects, [("paused-run-A", "approved-tool")] * 2)

    def test_same_stable_event_id_deduplicates_accepted_but_unacknowledged_send(self) -> None:
        queue = FakeQueue()
        retry_after_uncertain_delivery(
            queue, Resume("paused-run-A", "approved-tool", "resume:paused-run-A"),
            first="accept_then_lose_ack",
        )
        self.assertEqual(queue.deliveries, 2)
        self.assertEqual(queue.effects, [("paused-run-A", "approved-tool")])

    def test_rejected_before_acceptance_must_remain_retryable(self) -> None:
        queue = FakeQueue()
        retry_after_uncertain_delivery(
            queue, Resume("paused-run-A", "approved-tool", "resume:paused-run-A"),
            first="reject_before_accept",
        )
        self.assertEqual(queue.deliveries, 1)
        self.assertEqual(queue.effects, [("paused-run-A", "approved-tool")])

    def test_two_different_suspensions_must_both_run(self) -> None:
        queue = FakeQueue()
        queue.send(Resume("paused-run-A", "approved-tool", "resume:paused-run-A"))
        queue.send(Resume("paused-run-B", "approved-tool", "resume:paused-run-B"))
        self.assertEqual(len(queue.effects), 2)

    def test_global_event_id_would_wrongly_suppress_unrelated_approval(self) -> None:
        queue = FakeQueue()
        queue.send(Resume("paused-run-A", "approved-tool", "resume:any"))
        queue.send(Resume("paused-run-B", "approved-tool", "resume:any"))
        self.assertEqual(queue.effects, [("paused-run-A", "approved-tool")])
        # This is the *bad* design: an event ID must distinguish suspensions.


if __name__ == "__main__":
    unittest.main(verbosity=2)
