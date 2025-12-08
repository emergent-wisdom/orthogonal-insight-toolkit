#!/usr/bin/env python3
"""
Generate a random seed word for the Simulation Protocol.

Uses the system dictionary (~235k words) for true randomness.
The protocol works best when seeds feel irrelevant or uncomfortable.
"""

import random
import sys
import os

DICT_PATHS = [
    "/usr/share/dict/words",           # macOS, Linux
    "/usr/share/dict/american-english", # Debian/Ubuntu
    "/usr/share/dict/british-english",  # Debian/Ubuntu alt
]


def find_dictionary():
    """Find an available system dictionary."""
    for path in DICT_PATHS:
        if os.path.exists(path):
            return path
    return None


def load_dictionary(filter_mode="default"):
    """Load words from system dictionary with optional filtering."""

    dict_path = find_dictionary()

    if not dict_path:
        print("Warning: System dictionary not found. Using built-in list.", file=sys.stderr)
        return get_fallback_seeds()

    with open(dict_path, 'r') as f:
        words = [line.strip() for line in f]

    if filter_mode == "raw":
        # Everything, including proper nouns and obscure terms
        return words

    elif filter_mode == "default":
        # Lowercase only, 4-12 chars, no apostrophes
        return [
            w for w in words
            if w.islower()
            and 4 <= len(w) <= 12
            and "'" not in w
        ]

    elif filter_mode == "strict":
        # Common-ish words: lowercase, 5-10 chars, no rare suffixes
        rare_suffixes = ('ism', 'istic', 'ically', 'tion', 'ness', 'ment', 'ous')
        return [
            w for w in words
            if w.islower()
            and 5 <= len(w) <= 10
            and "'" not in w
            and not any(w.endswith(s) for s in rare_suffixes)
        ]

    return words


def get_fallback_seeds():
    """Fallback list if system dictionary unavailable."""
    return [
        'crystalline', 'molten', 'hollow', 'magnetic', 'buoyant', 'viscous',
        'transparent', 'porous', 'elastic', 'brittle', 'instantaneous', 'glacial',
        'cyclical', 'reversible', 'ephemeral', 'eternal', 'synchronized', 'staggered',
        'encrypted', 'verified', 'anonymous', 'broadcast', 'whispered', 'forgotten',
        'indelible', 'autonomous', 'choreographed', 'unanimous', 'anarchic', 'delegated',
        'centralized', 'emergent', 'deterministic', 'abundant', 'rationed', 'communal',
        'hoarded', 'renewable', 'depleting', 'borrowed', 'gifted', 'solitary', 'tribal',
        'mirrored', 'competitive', 'symbiotic', 'parasitic', 'apprenticed', 'ancestral',
        'mycelial', 'viral', 'metamorphic', 'dormant', 'migratory', 'territorial',
        'pollinating', 'decomposing', 'blindfolded', 'echoing', 'fragrant', 'numb',
        'synesthetic', 'magnified', 'inverted'
    ]


def pick_seed(filter_mode="default"):
    """Pick a random seed from the dictionary."""
    words = load_dictionary(filter_mode)
    return random.choice(words)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate a random seed word for the Simulation Protocol"
    )
    parser.add_argument(
        "-n", "--count",
        type=int,
        default=1,
        help="Number of seeds to generate (default: 1)"
    )
    parser.add_argument(
        "-m", "--mode",
        choices=["default", "raw", "strict"],
        default="default",
        help="Filter mode: default (~98k words), raw (235k), strict (~40k common)"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show dictionary statistics"
    )

    args = parser.parse_args()

    if args.stats:
        for mode in ["raw", "default", "strict"]:
            words = load_dictionary(mode)
            print(f"{mode}: {len(words):,} words")
        return

    for _ in range(args.count):
        print(pick_seed(args.mode))


if __name__ == "__main__":
    main()
