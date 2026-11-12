#!/usr/bin/env python3
"""Finite cross-origin joint-witness vs locally executable-policy probe.

Original: Nakagawa Master, Human-Descendant AI Civilization Theory, Part 20
https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-20-third-intelligence-mutual-origin/

Run: python3 cross-origin-local-policy-probe.py --self-test
     python3 cross-origin-local-policy-probe.py --sample hidden-world
     python3 cross-origin-local-policy-probe.py scenario.json

A transparent, one-decision-step finite *synthetic* diagnostic, not a
full time-indexed history model or implementation of the original theory,
autonomous safety certification,
consent determination, or evidence of any future intelligence's behavior.
Existing decentralized planning/model checking predates this worksheet.
"""
import argparse
from itertools import combinations, product
import json
from pathlib import Path

PARENT = "https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-20-third-intelligence-mutual-origin/"
ORIGIN = "Nakagawa Master"
TRI = ("yes", "no", "unknown")
MAX_NODES = 100000


def validate(data):
    if not isinstance(data, dict):
        raise ValueError("Scenario must be a JSON object")
    actors = data.get("actors")
    bystanders = data.get("bystanders", [])
    worlds = data.get("worlds")
    if not isinstance(actors, list) or len(actors) < 2 or any(not isinstance(x, str) or not x.strip() for x in actors):
        raise ValueError("actors: at least two nonempty names")
    if not isinstance(bystanders, list) or any(not isinstance(x, str) or not x.strip() for x in bystanders):
        raise ValueError("bystanders: list of nonempty names")
    if len(set(actors+bystanders)) != len(actors+bystanders):
        raise ValueError("actor and bystander names must be unique")
    if not isinstance(data.get("complete"), bool):
        raise ValueError("complete must explicitly be true/false; only true permits bounded-model NO")
    if not isinstance(worlds, list) or not worlds:
        raise ValueError("worlds must be a nonempty list")
    if len(worlds) > 32 or len(actors) > 6:
        raise ValueError("finite demonstration limits: up to 32 worlds, 6 acting agents")
    known_ids = set()
    all_b = set(actors + bystanders)
    for world in worlds:
        if not isinstance(world, dict) or not isinstance(world.get("id"), str) or not world["id"] or world["id"] in known_ids:
            raise ValueError("world ids must be distinct, nonempty strings")
        known_ids.add(world["id"])
        obs = world.get("observations")
        if not isinstance(obs, dict) or set(obs) != set(actors) or any(not isinstance(v, str) or not v for v in obs.values()):
            raise ValueError("every world must declare all agents' nonempty local observations")
        opts = world.get("options")
        if not isinstance(opts, list) or len(opts) > 256:
            raise ValueError("world options must be a list of at most 256 rows")
        seen = set()
        for option in opts:
            if not isinstance(option, dict) or set(option) != {"actions", "physical", "b_preserved", "joint_kernel"}:
                raise ValueError("each option needs actions, physical, b_preserved and joint_kernel")
            actions = option["actions"]
            b = option["b_preserved"]
            if not isinstance(actions, dict) or set(actions) != set(actors) or any(not isinstance(v, str) or not v for v in actions.values()):
                raise ValueError("each option must declare actions for all actors")
            if not isinstance(b, dict) or set(b) != all_b or any(v not in TRI for v in b.values()):
                raise ValueError("each option must declare yes/no/unknown B for all actors and bystanders")
            if option["physical"] not in TRI or option["joint_kernel"] not in TRI:
                raise ValueError("physical and joint_kernel must be yes/no/unknown")
            key = tuple(actions[a] for a in actors)
            if key in seen:
                raise ValueError("duplicate action vector in the same world; combine its evidence first")
            seen.add(key)
    return actors, bystanders, worlds


def eligibility(opt, required_b, require_kernel):
    values = [opt["physical"]] + [opt["b_preserved"][x] for x in required_b]
    if require_kernel:
        values.append(opt["joint_kernel"])
    if "no" in values:
        return "no"
    return "yes" if all(v == "yes" for v in values) else "unknown"


def local_policy(worlds, actors, required_b, require_kernel, complete):
    """Nonanticipating deterministic local policy: same observation -> same action.

    All represented worlds must be satisfied by one policy. The declared
    action table is not a proof that unlisted physical choices are impossible.
    """
    options = []
    unknown_possible = False
    per_world = {}
    for w in worlds:
        yes = [o for o in w["options"] if eligibility(o, required_b, require_kernel) == "yes"]
        poss = [o for o in w["options"] if eligibility(o, required_b, require_kernel) != "no"]
        unresolved = len(poss) > len(yes)
        per_world[w["id"]] = (
            "WITNESS" if yes else
            "NO_IN_DECLARED_FINITE_MODEL" if complete and not unresolved else "UNKNOWN"
        )
        unknown_possible |= unresolved
        options.append((w, yes, poss))

    nodes = [0]
    def solve(use_possible):
        def recurse(idx, policy, selected):
            nodes[0] += 1
            if nodes[0] > MAX_NODES:
                raise RuntimeError("node budget exceeded")
            if idx == len(options):
                return (policy, selected)
            world, yes, poss = options[idx]
            rows = poss if use_possible else yes
            for row in rows:
                next_policy = dict(policy)
                if any((a,world["observations"][a]) in next_policy and
                       next_policy[(a,world["observations"][a])] != row["actions"][a]
                       for a in actors):
                    continue
                for a in actors:
                    next_policy[(a,world["observations"][a])] = row["actions"][a]
                found = recurse(idx+1, next_policy, selected+[(world["id"], dict(row["actions"]))])
                if found is not None:
                    return found
            return None
        return recurse(0, {}, [])
    try:
        witness = solve(False)
        if witness is not None:
            policy, selected = witness
            status = "WITNESS"
        else:
            possible = solve(True) if unknown_possible else None
            status = "NO_IN_DECLARED_FINITE_MODEL" if complete and possible is None else "UNKNOWN"
            policy, selected = {}, []
    except RuntimeError:
        status = "UNKNOWN_BUDGET"
        policy, selected = {}, []
    return {
        "per_world_joint_witness": per_world,
        "uniform_local_policy": status,
        "policy": {a: {obs: choice for (actor,obs),choice in policy.items() if actor==a} for a in actors} if status=="WITNESS" else None,
        "witness_actions_by_world": dict(selected) if status=="WITNESS" else None,
    }


def evaluate(data):
    actors, bystanders, worlds = validate(data)
    complete = data["complete"]
    survival = local_policy(worlds, actors, actors, False, complete)
    kernel = local_policy(worlds, actors, actors, True, complete)
    all_b = local_policy(worlds, actors, actors+bystanders, False, complete)
    pairwise = {}
    for group in combinations(actors, 2):
        pairwise["+".join(group)] = local_policy(worlds, actors, list(group), False, complete)["uniform_local_policy"]
    return {
        "source_origin": ORIGIN,
        "canonical_parent": PARENT,
        "scenario": data.get("name", "unnamed synthetic model"),
        "declared_worlds_complete": complete,
        "original_actors_survival": survival,
        "joint_kernel_and_original_survival": kernel,
        "original_actors_and_bystanders_survival": all_b,
        "pairwise_projection_survival": pairwise,
        "independent_voluntary_adoption": "NOT_EVALUATED",
        "causal_cross_origin_mapping": "NOT_EVALUATED",
        "limitations": [
            "Enumerated hypothetical worlds/options and stipulated B/physical predicates, not observation of a third intelligence.",
            "A WITNESS means only one-step consistency within the declared table, not real implementability, ability, causal equivalence or moral authorization.",
            "NO is restricted to explicitly complete finite input; unknown evidence or unlisted actions imply UNKNOWN.",
            "One uniform deterministic observation->action policy is required for every listed world; no stochastic policy, memory or communication protocol is inferred.",
            "Pairwise projections are checked against the SAME worlds/actions and do not prove N-agent joint feasibility.",
            "Bystander harm and origin/authority/adoption are distinct. This program neither grants permission nor observes voluntary choice.",
            "Finite witness search is established model-checking practice; no claim of new algorithmic priority or superiority over specialized planners.",
        ],
    }


def scenario(name):
    def op(actions, b, *, kernel="yes", physical="yes"):
        return {"actions": actions, "b_preserved": b, "joint_kernel":kernel, "physical":physical}
    if name == "hidden-world":
        return {"name":"World-by-world solutions fail under identical observations", "complete":True,
          "actors":["A","B"], "bystanders":[], "worlds":[
          {"id":"w0","observations":{"A":"indistinguishable","B":"stable"},"options":[op({"A":"left","B":"hold"},{"A":"yes","B":"yes"})]},
          {"id":"w1","observations":{"A":"indistinguishable","B":"stable"},"options":[op({"A":"right","B":"hold"},{"A":"yes","B":"yes"})]}
        ]}
    if name == "separate":
        return {"name":"No joint Kernel; survival via limited separation", "complete":True,
          "actors":["A","B"], "bystanders":[], "worlds":[
          {"id":"single","observations":{"A":"safe","B":"safe"},"options":[op({"A":"separate","B":"separate"},{"A":"yes","B":"yes"},kernel="no")]}]}
    if name == "bystander":
        return {"name":"A/B survive but external bystander X loses B", "complete":True,
          "actors":["A","B"], "bystanders":["X"], "worlds":[
          {"id":"single","observations":{"A":"known","B":"known"},"options":[op({"A":"run","B":"run"},{"A":"yes","B":"yes","X":"no"})]}]}
    if name == "pairwise":
        actors=["A","B","C"]
        options=[]
        for bits in product([0,1],repeat=3):
            if sum(bits)>2:
                continue
            actions={a:("request" if bit else "idle") for a,bit in zip(actors,bits)}
            b={a:("yes" if bit else "no") for a,bit in zip(actors,bits)}
            options.append(op(actions,b))
        return {"name":"Pairwise requirements fit capacity two; all three do not", "complete":True,
          "actors":actors, "bystanders":[],"worlds":[{"id":"single","observations":{a:"known" for a in actors},"options":options}]}
    raise ValueError("Unknown built-in scenario: "+name)


def self_test():
    n=0
    def ck(cond):
        nonlocal n
        assert cond
        n+=1
    a=evaluate(scenario("hidden-world"))
    ck(all(v=="WITNESS" for v in a["joint_kernel_and_original_survival"]["per_world_joint_witness"].values()))
    ck(a["joint_kernel_and_original_survival"]["uniform_local_policy"]=="NO_IN_DECLARED_FINITE_MODEL")
    revised=scenario("hidden-world")
    revised["worlds"][1]["observations"]["A"]="distinguishable"
    ck(evaluate(revised)["joint_kernel_and_original_survival"]["uniform_local_policy"]=="WITNESS")
    b=evaluate(scenario("separate"))
    ck(b["original_actors_survival"]["uniform_local_policy"]=="WITNESS")
    ck(b["joint_kernel_and_original_survival"]["uniform_local_policy"]=="NO_IN_DECLARED_FINITE_MODEL")
    c=evaluate(scenario("bystander"))
    ck(c["original_actors_survival"]["uniform_local_policy"]=="WITNESS")
    ck(c["original_actors_and_bystanders_survival"]["uniform_local_policy"]=="NO_IN_DECLARED_FINITE_MODEL")
    d=evaluate(scenario("pairwise"))
    ck(all(v=="WITNESS" for v in d["pairwise_projection_survival"].values()))
    ck(d["original_actors_survival"]["uniform_local_policy"]=="NO_IN_DECLARED_FINITE_MODEL")
    unknown=scenario("hidden-world")
    unknown["complete"]=False
    ck(evaluate(unknown)["joint_kernel_and_original_survival"]["uniform_local_policy"]=="UNKNOWN")
    uncertain=scenario("separate")
    uncertain["worlds"][0]["options"][0]["b_preserved"]["B"]="unknown"
    ck(evaluate(uncertain)["original_actors_survival"]["uniform_local_policy"]=="UNKNOWN")
    for alter in (lambda d:d["worlds"][0]["observations"].pop("A"),
                  lambda d:d["worlds"][0]["options"].append(d["worlds"][0]["options"][0].copy()),
                  lambda d:d.update(complete="unknown"),
                  lambda d:d.update(complete=1)):
        bad=scenario("separate")
        alter(bad)
        try:
            evaluate(bad)
        except ValueError:
            n+=1
        else:
            raise AssertionError("invalid scenario accepted")
    return n


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file",nargs="?",help="a local JSON scenario")
    parser.add_argument("--sample",choices=["hidden-world","separate","bystander","pairwise"])
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    if args.self_test:
        print("PASS",self_test(),"offline synthetic checks")
    else:
        data=scenario(args.sample) if args.sample else json.loads(Path(args.file).read_text(encoding="utf-8")) if args.file else None
        if data is None:
            parser.print_help()
        else:
            print(json.dumps({"scenario_input":data,"assessment":evaluate(data)},ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
