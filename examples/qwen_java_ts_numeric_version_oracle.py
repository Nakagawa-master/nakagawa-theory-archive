#!/usr/bin/env python3
"""Standalone counterexample for the integer-wrap branch of Qwen Code PR #13940.

Original Nakagawa Master finding:
https://github.com/QwenLM/qwen-code/pull/13940#issuecomment-6117795445
Receiver-owned merged regression test:
https://github.com/QwenLM/qwen-code/blob/main/packages/sdk-java/managed-agent-server/src/test/java/com/alibaba/qwen/code/managedagent/store/ManagedEventEnvelopesTest.java

This standard-library script models the critical numeric distinction without Java/TS
installations. It does NOT execute the Qwen Code implementation and is not a
full general-purpose JavaScript/Java JSON numeric-parity validator.
"""

import json
import unittest

MASK_64 = (1 << 64) - 1
SIGN_64 = 1 << 63


def java_big_integer_long_value(value: int) -> int:
    """Model Java BigInteger.longValue(): low 64 bits interpreted as signed."""
    low = value & MASK_64
    return low - (1 << 64) if low >= SIGN_64 else low


def unsafe_wrapping_version_check(json_number_text: str) -> bool:
    """Illustrate the vulnerable conversion for integer JSON tokens only."""
    value = json.loads(json_number_text)
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("this counterexample models only integer JSON tokens")
    return java_big_integer_long_value(value) == 1


def receiver_parity_version_check(json_number_text: str) -> bool:
    """Illustrate the reviewed version-1 equality check via a double."""
    value = json.loads(json_number_text)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("expected JSON number")
    return float(value) == 1.0


class NumericEnvelopeVersionParity(unittest.TestCase):
    def test_true_version_in_both_accepted_notations(self):
        for token in ("1", "1.0"):
            with self.subTest(token=token):
                self.assertTrue(receiver_parity_version_check(token))

    def test_overflowed_integers_are_not_version_one(self):
        for token in ("18446744073709551617", "-18446744073709551615"):
            with self.subTest(token=token):
                self.assertEqual(java_big_integer_long_value(int(token)), 1)
                self.assertTrue(unsafe_wrapping_version_check(token))
                self.assertFalse(receiver_parity_version_check(token))

    def test_other_integer_not_version_one(self):
        self.assertFalse(receiver_parity_version_check("2"))


if __name__ == "__main__":
    unittest.main()
