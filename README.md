# Orthogonal Insight Protocol Toolkit

Generate non-obvious solutions by changing the physics of your problem.

## What Is This?

The Orthogonal Insight Protocol escapes "median" AI answers by:
1. **Build a world** with impossible physics (from a random seed word)
2. **Solve the problem** inside that world (with a fresh, blind agent)
3. **Extract the mechanism** — the abstract principle that made it work
4. **Bridge to reality** — implement the mechanism in the real world

**Key insight:** Temperature gives you different words. Seeds give you different logic.

## Quick Start (Claude Code)

1. Clone this repo and open in Claude Code:
   ```bash
   git clone https://github.com/emergent-wisdom/orthogonal-insight-toolkit
   cd orthogonal-insight-toolkit
   claude
   ```

2. Describe your problem:
   ```
   How can we reduce loneliness in cities?
   ```

Claude Code will spawn separate agents for each phase (world builder, solver, extractor) to ensure blind operation.

## Installation

Just clone and open - the CLAUDE.md file tells Claude how to run the protocol.

## How It Works

### The Problem with Temperature

When you crank up AI temperature, you get lexical diversity — different words for similar ideas. The model is still "standing in the same spot."

### The Solution: Semantic Seeds

When you seed with impossible world constraints ("everything is porous", "violence mirrors back on the actor"), you get semantic diversity — genuinely different problem frames.

### Why Fresh Agents Matter

Each phase uses a **separate agent** with no shared context:
- World Builder knows only the seed (not the problem)
- Solver knows only the world rules (not the seed)
- Extractor knows only the solution (not the experiment)

This prevents contamination. The blind architecture forces genuine divergence.

## Examples

### Loneliness × POROUS

**Problem:** Epidemic of loneliness
**Seed:** POROUS (nothing maintains boundaries)

**Standard approach:** More social programs, dating apps, community centers

**OIP insight:** In a porous world, loneliness itself is the contagion spreading through connections. It's not a connection deficit — it's a transmission problem.

**Bridge to reality:** Cacioppo's Framingham study (2009) found loneliness spreads through social networks like a contagion. Train "loneliness composters" who absorb and transform it.

### Antibiotics × MIRRORED

**Problem:** Antibiotic resistance
**Seed:** MIRRORED (all actions reflect back on the actor)

**Standard approach:** Use antibiotics more carefully

**OIP insight:** In a mirrored world, you can't attack pathogens at all. You must make beneficial bacteria outcompete harmful ones.

**Bridge to reality:** Fecal microbiota transplants, quorum sensing disruption, environmental optimization over direct intervention.

## When to Use This

- You keep getting the same obvious answers
- The problem feels "stuck" in a particular framing
- You want to challenge assumptions
- The value of a breakthrough is 100x a standard improvement

## When NOT to Use This

- Simple/routine tasks
- The obvious solution is correct
- You need a quick answer

Don't use the Orthogonal Insight Protocol to build a toaster. Use it to invent the microwave.

## Credits

Based on "Orthogonal Insight Protocol" by Henrik Westerberg.

## License

MIT
