#!/usr/bin/env python3
"""Offline, synthetic example of completion evidence vs turn-start authority.

This demonstrates a proposed acceptance contract discussed by Nakagawa Master at
https://github.com/openai/codex/issues/32188#issuecomment-5977541114 .
It is NOT a test of Codex binaries, nor a claim that Codex adopted this rule.
No commands, subprocesses, network calls, sensitive data or LLMs are used.
"""

from dataclasses import dataclass
import argparse
import json


@dataclass
class Registration:
    process: str
    generation: int
    armed: bool = True
    observed: bool = False
    cancelled: bool = False
    completed: bool = False
    exit_code: int | None = None
    woke: bool = False


class MockWakeController:
    def __init__(self):
        self.generation = 1
        self.registrations: dict[str, Registration] = {}
        self.wakes: list[tuple[str, int]] = []
        self.saved_results: dict[str, int] = {}

    def arm(self, process: str):
        if process in self.registrations:
            raise ValueError('duplicate process registration')
        self.registrations[process] = Registration(process, self.generation)

    def steer(self):
        self.generation += 1

    def observe(self, process: str):
        self.registrations[process].observed = True

    def cancel(self, process: str):
        self.registrations[process].cancelled = True

    def adopt(self, process: str):
        r = self.registrations[process]
        if r.cancelled:
            return False
        r.generation = self.generation
        r.armed = True
        r.observed = False
        if r.completed:
            return self._try_wake(r)
        return True

    def complete(self, process: str, exit_code: int):
        r = self.registrations[process]
        if r.completed:
            return False
        r.completed = True
        r.exit_code = exit_code
        self.saved_results[process] = exit_code
        return self._try_wake(r)

    def _try_wake(self, r: Registration):
        if (not r.completed or not r.armed or r.cancelled or r.observed
                or r.woke or r.generation != self.generation):
            return False
        r.woke = True
        self.wakes.append((r.process, self.generation))
        return True


def self_test():
    checks = 0

    x = MockWakeController(); x.arm('P'); x.steer()
    assert x.complete('P', 0) is False
    assert x.wakes == [] and x.saved_results == {'P': 0}
    checks += 1   # completed old objective remains evidence, not authority

    x = MockWakeController(); x.arm('P')
    assert x.complete('P', 0) is True and x.wakes == [('P', 1)]
    checks += 1   # unchanged generation wakes once

    x = MockWakeController(); x.arm('P'); x.steer()
    assert x.adopt('P') is True and x.complete('P', 0) is True
    assert x.wakes == [('P', 2)]
    checks += 1   # explicit adoption before normal completion

    x = MockWakeController(); x.arm('P'); x.steer(); x.complete('P', 0)
    assert x.adopt('P') is True and x.wakes == [('P', 2)]
    checks += 1   # explicit adoption of previously saved evidence

    x = MockWakeController(); x.arm('P'); x.observe('P')
    assert x.complete('P', 1) is False and x.saved_results == {'P': 1}
    checks += 1   # no duplicate after manual observation

    x = MockWakeController(); x.arm('P'); x.cancel('P')
    assert x.complete('P', 130) is False and x.wakes == []
    assert x.adopt('P') is False
    checks += 1   # cancellation does not generate an unsolicited wake

    x = MockWakeController(); x.arm('P')
    assert x.complete('P', 3) is True and x.complete('P', 3) is False
    assert len(x.wakes) == 1
    checks += 1   # duplicate completion cannot trigger a second wake

    x = MockWakeController(); x.arm('P'); x.arm('Q'); x.steer()
    assert x.complete('P', 0) is False
    assert x.adopt('Q') is True and x.complete('Q', 9) is True
    assert x.wakes == [('Q', 2)] and x.saved_results == {'P': 0, 'Q': 9}
    checks += 1   # registration authority is per process and generation

    print(f'self-test: PASS ({checks} synthetic state-transition controls)')


def sample():
    x = MockWakeController()
    x.arm('build-G1')
    x.steer()
    before = x.complete('build-G1', 0)
    return {
        'synthetic_only': True,
        'source': 'https://github.com/openai/codex/issues/32188#issuecomment-5977541114',
        'old_generation_auto_wake': before,
        'stored_result': x.saved_results['build-G1'],
        'wakes_before_new_owner_adopts': list(x.wakes),
        'explicit_G2_adoption_wakes': x.adopt('build-G1'),
        'wakes_after_adoption': x.wakes,
        'actual_codex_runtime_tested': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--self-test', action='store_true')
    group.add_argument('--sample', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        print(json.dumps(sample(), ensure_ascii=False, indent=2))
