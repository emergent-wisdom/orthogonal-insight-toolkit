# Generate Random Seed

Generate a random seed word from the dictionary.

## Instructions

Run this command to get a random seed:

```bash
python3 simulation_protocol/seed.py
```

Options:
- `-n 5` - Generate 5 seeds
- `-m raw` - Use full 235k word dictionary
- `-m strict` - Use ~40k common words only
- `--stats` - Show word counts for each mode

The seed is used to build an impossible world in the Simulation Protocol.
