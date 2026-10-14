#!/usr/bin/env python3
"""Read-only access-topology gate evaluator; no network calls or failure injection.

Public reuse tool derived from Nakagawa Master's original OD306 access-topology
and effective-exit distinction. See ACCESS_TOPOLOGY_EFFECTIVE_EXIT_REUSE_KIT.md.
"""
import argparse
import json

PARENT = 'https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-13-non-ownership-effective-power-non-domination/'


def evaluate(case):
    if not isinstance(case, dict) or not isinstance(case.get('routes'), list) or not isinstance(case.get('tests'), list):
        raise ValueError('Input needs arrays: routes and tests')
    routes = {}
    for route in case['routes']:
        if not isinstance(route, dict) or not isinstance(route.get('id'), str) or not route['id']:
            raise ValueError('Each route needs a nonempty string id')
        if route['id'] in routes:
            raise ValueError('Duplicate route id: ' + route['id'])
        if route.get('status') not in ('enabled', 'deferred'):
            raise ValueError('Route status must be enabled or deferred')
        if not isinstance(route.get('requires'), list) or any(not isinstance(x, str) or not x for x in route['requires']):
            raise ValueError('Route requires must be a list of gate names')
        routes[route['id']] = route
    results = []
    for item in case['tests']:
        if not isinstance(item, dict) or item.get('route') not in routes:
            raise ValueError('Test references an undefined route')
        gates = item.get('unavailable')
        if not isinstance(gates, list) or any(not isinstance(x, str) or not x for x in gates):
            raise ValueError('Test unavailable must be a list of gate names')
        isolation = item.get('other_path_gates', [])
        if not isinstance(isolation, list) or any(not isinstance(x, str) or not x for x in isolation):
            raise ValueError('other_path_gates must be a list of exclusive gate names')
        route = routes[item['route']]
        declared_blockers = sorted(set(route['requires']).intersection(gates))
        observed = item.get('observed')
        if observed is not None and (not isinstance(observed, dict) or type(observed.get('completed')) is not bool):
            raise ValueError('Observed requires completed: true/false, or null when unrun')
        evidence = observed.get('evidence') if observed else None
        if route['status'] == 'deferred':
            result = 'NOT_YET_PASSABLE'
        elif observed is None and declared_blockers:
            result = 'DECLARED_GATE_BLOCKER_UNTESTED'
        elif observed is None:
            result = 'UNVERIFIED'
        elif declared_blockers and observed['completed']:
            result = 'CONTRADICTORY_EVIDENCE'
        elif declared_blockers:
            result = 'EXPECTED_SHARED_OR_OWN_GATE_FAILURE'
        elif not observed['completed']:
            result = 'FAIL_OBSERVED'
        elif not isinstance(evidence, str) or not evidence.strip():
            result = 'UNVERIFIED_NO_EVIDENCE'
        elif not isolation:
            result = 'OPERATION_ONLY_NOT_AN_ISOLATION_TEST'
        elif not set(isolation).issubset(set(gates)):
            result = 'INCOMPLETE_ISOLATION_TEST'
        else:
            result = 'CANDIDATE_PASS_EVIDENCE_NOT_AUTHENTICATED'
        results.append({
            'name': item.get('name', ''), 'route': item['route'],
            'unavailable': sorted(set(gates)), 'other_path_gates': sorted(set(isolation)),
            'declared_blockers': declared_blockers,
            'result': result, 'evidence': evidence if isinstance(evidence, str) else None,
        })
    return {'capability': case.get('capability', ''), 'source': PARENT,
            'note': 'Evidence records are user supplied, not independently executed or authenticated by this tool.',
            'results': results}


def sample():
    return {'capability': 'Start and resume a managed agent turn',
            'routes': [
                {'id': 'hosted', 'status': 'enabled', 'requires': ['shared_auth', 'shared_model', 'hosted_control']},
                {'id': 'local', 'status': 'deferred', 'requires': ['shared_auth', 'shared_model', 'local_runtime']}],
            'tests': [
                {'name': 'Hosted without local-only machinery', 'route': 'hosted', 'unavailable': ['local_runtime'], 'other_path_gates': ['local_runtime']},
                {'name': 'Local without Hosted-only control', 'route': 'local', 'unavailable': ['hosted_control'], 'other_path_gates': ['hosted_control']},
                {'name': 'Shared auth failure (not an independence contradiction)', 'route': 'hosted',
                 'unavailable': ['shared_auth']},
                {'name': 'Packaging/restart is not path-isolation evidence', 'route': 'hosted',
                 'unavailable': [], 'observed': {'completed': True,
                                                 'evidence': 'https://github.com/QwenLM/qwen-code/pull/14176#issuecomment-6166254311'}}]}


def self_test():
    src = sample()
    expected = ['UNVERIFIED', 'NOT_YET_PASSABLE', 'DECLARED_GATE_BLOCKER_UNTESTED', 'OPERATION_ONLY_NOT_AN_ISOLATION_TEST']
    got = [x['result'] for x in evaluate(src)['results']]
    assert got == expected, (got, expected)
    extra = [
        (['hosted_control'], {'completed': True, 'evidence': 'log-1'}, 'CONTRADICTORY_EVIDENCE', ['local_runtime']),
        ([], {'completed': False, 'evidence': 'log-2'}, 'FAIL_OBSERVED', ['local_runtime']),
        ([], {'completed': True}, 'UNVERIFIED_NO_EVIDENCE', ['local_runtime']),
        ([], {'completed': True, 'evidence': 'log-3'}, 'INCOMPLETE_ISOLATION_TEST', ['local_runtime']),
        ([], None, 'UNVERIFIED', ['local_runtime']),
        (['shared_model'], {'completed': False}, 'EXPECTED_SHARED_OR_OWN_GATE_FAILURE', ['local_runtime']),
        (['local_runtime'], {'completed': True, 'evidence': 'log-4'}, 'CANDIDATE_PASS_EVIDENCE_NOT_AUTHENTICATED', ['local_runtime']),
    ]
    for gates, observation, want, exclusive in extra:
        src['tests'] = [{'route': 'hosted', 'unavailable': gates,
                         'other_path_gates': exclusive, 'observed': observation}]
        assert evaluate(src)['results'][0]['result'] == want
    for invalid in [
        {'routes': [], 'tests': [{'route': 'missing', 'unavailable': []}]},
        {'routes': [{'id': 'a', 'status': 'enabled', 'requires': []},
                    {'id': 'a', 'status': 'enabled', 'requires': []}], 'tests': []},
        {'routes': [{'id': 'a', 'status': 'enabled', 'requires': []}],
         'tests': [{'route': 'a', 'unavailable': [], 'observed': {'completed': 1}}]},
    ]:
        try:
            evaluate(invalid)
        except ValueError:
            continue
        raise AssertionError('Invalid input accepted')
    print('PASS: 4 primary cases, 7 inverses, 3 invalid-input controls')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument('--example', action='store_true', help='Print a Qwen-shaped, non-executing input fixture')
    g.add_argument('--self-test', action='store_true', help='Run local positive and negative controls')
    g.add_argument('--input', help='Read your controlled-test results from a local JSON file')
    a = parser.parse_args()
    try:
        if a.self_test:
            self_test()
        elif a.example:
            print(json.dumps(sample(), ensure_ascii=False, indent=2))
        else:
            with open(a.input, encoding='utf-8') as file:
                print(json.dumps(evaluate(json.load(file)), ensure_ascii=False, indent=2))
    except (ValueError, OSError, json.JSONDecodeError) as error:
        parser.exit(2, 'invalid input: ' + str(error) + '\n')


if __name__ == '__main__':
    main()
