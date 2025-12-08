#!/usr/bin/env python3
"""
Run the full Simulation Protocol pipeline.

Each phase uses a fresh API call (stateless = blind agent).
"""

import sys
import os
import json
from datetime import datetime

from .seed import pick_seed
from .prompts import WORLD_BUILDER, SOLVER, EXTRACTOR, CONTROL


def get_client():
    """Get Anthropic client, with helpful error if not installed."""
    try:
        import anthropic
        return anthropic.Anthropic()
    except ImportError:
        print("Error: anthropic package not installed.", file=sys.stderr)
        print("Install with: pip install simulation-protocol[api]", file=sys.stderr)
        sys.exit(1)
    except anthropic.AuthenticationError:
        print("Error: ANTHROPIC_API_KEY not set or invalid.", file=sys.stderr)
        sys.exit(1)


def call_llm(client, prompt: str, model: str = "claude-sonnet-4-20250514") -> str:
    """Make a single stateless API call (fresh agent)."""
    response = client.messages.create(
        model=model,
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text


def run_protocol(problem: str, seed: str = None, model: str = "claude-sonnet-4-20250514",
                 include_control: bool = True, verbose: bool = True) -> dict:
    """
    Run the full Simulation Protocol.

    Each phase is a fresh API call - no context shared between agents.
    Only the necessary output is passed forward.
    """
    client = get_client()

    # Generate seed if not provided
    if seed is None:
        seed = pick_seed()

    if verbose:
        print(f"Seed: {seed.upper()}")
        print(f"Problem: {problem}")
        print("-" * 50)

    results = {
        "seed": seed,
        "problem": problem,
        "model": model,
        "timestamp": datetime.now().isoformat(),
    }

    # Phase 1: World Builder (knows only seed)
    if verbose:
        print("Phase 1: Building world...")

    world_prompt = WORLD_BUILDER.format(seed=seed)
    world_rules = call_llm(client, world_prompt, model)
    results["world_rules"] = world_rules

    if verbose:
        print("  Done.")

    # Phase 2: Solver (knows only world rules + problem)
    if verbose:
        print("Phase 2: Solving in-world...")

    solver_prompt = SOLVER.format(world_rules=world_rules, problem=problem)
    solution = call_llm(client, solver_prompt, model)
    results["solution"] = solution

    if verbose:
        print("  Done.")

    # Phase 3: Extractor (knows only solution + rules)
    if verbose:
        print("Phase 3: Extracting mechanism...")

    extractor_prompt = EXTRACTOR.format(solution=solution, world_rules=world_rules)
    mechanism = call_llm(client, extractor_prompt, model)
    results["mechanism"] = mechanism

    if verbose:
        print("  Done.")

    # Phase 4: Control (optional baseline)
    if include_control:
        if verbose:
            print("Phase 4: Getting control response...")

        control_prompt = CONTROL.format(expert_type="domain", problem=problem)
        control = call_llm(client, control_prompt, model)
        results["control"] = control

        if verbose:
            print("  Done.")

    return results


def format_report(results: dict) -> str:
    """Format results as markdown report."""
    report = f"""# Simulation Protocol Report

**Problem:** {results['problem']}
**Seed:** {results['seed'].upper()}
**Model:** {results['model']}
**Timestamp:** {results['timestamp']}

---

## Phase 1: World Rules ({results['seed'].upper()})

{results['world_rules']}

---

## Phase 2: In-World Solution

{results['solution']}

---

## Phase 3: Mechanism Extraction

{results['mechanism']}
"""

    if 'control' in results:
        report += f"""
---

## Control Response (Standard Approach)

{results['control']}
"""

    return report


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Run the Simulation Protocol to generate non-obvious solutions"
    )
    parser.add_argument(
        "problem",
        help="The problem to solve (in quotes)"
    )
    parser.add_argument(
        "-s", "--seed",
        help="Specific seed word (default: random)"
    )
    parser.add_argument(
        "-m", "--model",
        default="claude-sonnet-4-20250514",
        help="Model to use (default: claude-sonnet-4-20250514)"
    )
    parser.add_argument(
        "--no-control",
        action="store_true",
        help="Skip the control comparison"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file (default: stdout)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON instead of markdown"
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress progress messages"
    )

    args = parser.parse_args()

    results = run_protocol(
        problem=args.problem,
        seed=args.seed,
        model=args.model,
        include_control=not args.no_control,
        verbose=not args.quiet
    )

    if args.json:
        output = json.dumps(results, indent=2)
    else:
        output = format_report(results)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        if not args.quiet:
            print(f"\nReport saved to: {args.output}")
    else:
        print("\n" + "=" * 50)
        print(output)


if __name__ == "__main__":
    main()
