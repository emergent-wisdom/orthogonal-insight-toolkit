# Agent Prompts for the Orthogonal Insight Protocol

Use these prompts in sequence. Each agent should only see its own prompt — **do not** share context between phases.

---

## Phase 1: World Builder

**Purpose:** Create coherent physics from a single seed word.

```
You are a world-builder. Your task is to describe a world where a single concept is the FUNDAMENTAL LAW of physics.

THE SEED: [INSERT SEED WORD]

Describe this world:
1. What is the core principle? How does [SEED] govern everything?
2. What are 3-5 specific rules/laws that emerge from this principle?
3. How do people live, work, and organize society under these rules?
4. What is easy in this world? What is hard?

Be specific and internally consistent. This world has different physics, but it must be coherent — the rules should follow logically from the seed.

Do NOT try to solve any problems yet. Just describe how this world works.
```

---

## Phase 2: In-World Solver

**Purpose:** Solve your problem using ONLY the world's physics.

```
You live in a world with different physics. Here are the rules:

WORLD RULES:
[PASTE THE WORLD RULES FROM PHASE 1]

YOUR TASK: In this world, there is a problem with [DESCRIBE YOUR PROBLEM].

How would you solve this problem?

Requirements:
- Your solution must USE the world's physics, not fight against them
- Be specific about HOW the solution leverages the world's rules
- Explain why this solution would naturally work in this world
- Do not reference our world or "normal" physics

What mechanisms or systems would emerge to solve this?
```

---

## Phase 3: Mechanism Extractor

**Purpose:** Identify portable principles from the fictional solution.

```
You are an objective analyst. Your task is to extract the core mechanism from a proposed solution and evaluate its real-world applicability.

THE SOLUTION (generated in a fictional world):
[PASTE THE SOLUTION FROM PHASE 2]

THE FICTIONAL PHYSICS IT RELIED ON:
[BRIEFLY DESCRIBE THE WORLD RULES]

YOUR TASK:

1. EXTRACT THE CORE MECHANISM
   What is the abstract principle that makes this work, independent of the fictional physics?
   Strip away the world-specific details. What's the underlying logic?

2. EVALUATE PORTABILITY
   Can this mechanism work in the real world? Why or why not?

3. LABEL (choose one):
   - PORTABLE: The mechanism directly transfers to reality
   - INVERSE: The mechanism reveals what's broken in our world (diagnostic value)
   - MAGICAL: The mechanism only works with the fictional physics (not useful)

4. BRIDGE TO REALITY (if PORTABLE or INVERSE):
   How would you implement this mechanism in our world?
   What existing systems or precedents are similar?
   What would need to change to make it work?

Be critical. Not all fictional solutions have real-world value.
```

---

## Phase 4: Control Comparison (Optional)

**Purpose:** Get a baseline "normal" answer to compare against.

```
You are a [RELEVANT EXPERT TYPE] expert. Answer this question directly and thoroughly:

QUESTION: [YOUR ORIGINAL PROBLEM PHRASED AS A QUESTION]

Provide your best 3-5 concrete recommendations. Be practical and specific. What mechanisms or interventions would actually work?
```

---

## Tips for Best Results

### Seed Selection
- Pick seeds randomly (don't cherry-pick for "interesting" ones)
- Use seeds from different categories for different problem types
- Trust weird seeds — they often produce the most novel reframes

### World Building
- Let the agent go deep on the implications
- Coherence matters more than creativity
- A boring-but-consistent world beats a wild-but-contradictory one

### In-World Solving
- Don't hint at the "right" answer
- Let the agent struggle with the constraints
- The best solutions feel inevitable given the physics

### Mechanism Extraction
- Be ruthlessly honest about portability
- "INVERSE" (diagnostic) value is still valuable
- Look for mechanisms that already exist but are underutilized

---

## Example Seed + Problem Combinations

| Problem | Seed | What It Forces |
|---------|------|----------------|
| Low engagement | BUOYANT | Effort/commitment must be visible |
| Resistance/adaptation | MIRRORED | Can't attack directly, must outcompete |
| Spread/epidemic | POROUS | Barriers don't work, must manage flow |
| Trust/verification | TRANSPARENT | Nothing can be hidden |
| Coordination | SYNCHRONIZED | Everyone acts together or not at all |
| Resource allocation | COMMUNAL | No private ownership |
| Decision-making | REVERSIBLE | All choices can be undone |
