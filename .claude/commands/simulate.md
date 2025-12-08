# Run Simulation Protocol

Run the full Simulation Protocol on a problem.

## Arguments
- $ARGUMENTS: The problem to solve

## Instructions

You are running the Simulation Protocol. This generates non-obvious solutions by forcing the problem through an impossible world.

**CRITICAL: You must spawn separate agents for each phase using the Task tool. Do not solve in your own context - each agent must be blind to the others.**

### Step 1: Generate Seed
Run:
```bash
python3 simulation_protocol/seed.py
```

### Step 2: Spawn World Builder
Use Task tool with subagent_type="general-purpose":
```
You are a world-builder. Describe a world where [SEED] is the FUNDAMENTAL LAW of physics.

1. The core principle - how does [SEED] govern everything?
2. 3-5 specific rules/laws
3. How people live and work under these rules
4. What is easy? What is hard?

Be internally consistent. Do NOT solve any problems yet.
```

### Step 3: Spawn Solver
Use Task tool with subagent_type="general-purpose":
```
You live in a world with these physics:
[WORLD RULES FROM STEP 2]

Problem: $ARGUMENTS

Solve this using the world's physics. Do not reference normal physics.
```

### Step 4: Spawn Extractor
Use Task tool with subagent_type="general-purpose":
```
Extract the mechanism from this solution:
[SOLUTION FROM STEP 3]

World physics it relied on:
[WORLD RULES FROM STEP 2]

1. What abstract principle makes this work?
2. Label: PORTABLE, INVERSE, or MAGICAL
3. How to implement in reality?
```

### Step 5: Present Results
Summarize for the user:
- The seed and world
- The in-world solution
- The extracted mechanism and its portability
- How it differs from obvious approaches
