"""Prompt templates for each phase of the Simulation Protocol."""

WORLD_BUILDER = """You are a world-builder. Your task is to describe a world where a single concept is the FUNDAMENTAL LAW of physics.

THE SEED: {seed}

Describe this world:
1. What is the core principle? How does {seed} govern everything?
2. What are 3-5 specific rules/laws that emerge from this principle?
3. How do people live, work, and organize society under these rules?
4. What is easy in this world? What is hard?

Be specific and internally consistent. This world has different physics, but it must be coherent — the rules should follow logically from the seed.

Do NOT try to solve any problems yet. Just describe how this world works."""


SOLVER = """You live in a world with different physics. Here are the rules:

WORLD RULES:
{world_rules}

YOUR TASK: In this world, there is a problem: {problem}

How would you solve this problem?

Requirements:
- Your solution must USE the world's physics, not fight against them
- Be specific about HOW the solution leverages the world's rules
- Explain why this solution would naturally work in this world
- Do not reference our world or "normal" physics

What mechanisms or systems would emerge to solve this?"""


EXTRACTOR = """You are an objective analyst. Your task is to extract the core mechanism from a proposed solution and evaluate its real-world applicability.

THE SOLUTION (generated in a fictional world):
{solution}

THE FICTIONAL PHYSICS IT RELIED ON:
{world_rules}

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

Be critical. Not all fictional solutions have real-world value."""


CONTROL = """You are a {expert_type} expert. Answer this question directly and thoroughly:

QUESTION: {problem}

Provide your best 3-5 concrete recommendations. Be practical and specific. What mechanisms or interventions would actually work?"""
