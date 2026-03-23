#!/usr/bin/env python3

import random


ALL_ACHIEVEMENTS = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder", "Champion", "Legend",
]

PLAYER_NAMES = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_player_achievements() -> set:
    count = random.randint(4, len(ALL_ACHIEVEMENTS) - 2)
    return set(random.sample(ALL_ACHIEVEMENTS, count))


def get_all_unique(players: dict) -> set:
    all_achievements = set()
    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)
    return all_achievements


def get_common_all(players: dict) -> set:
    sets = list(players.values())
    common = sets[0]
    for i in range(1, len(sets)):
        common = common.intersection(sets[i])
    return common


def get_exclusive(name: str, players: dict) -> set:
    others = set()
    for other_name in players:
        if other_name != name:
            others = others.union(players[other_name])
    return players[name].difference(others)


def get_missing(name: str, players: dict) -> set:
    return set(ALL_ACHIEVEMENTS).difference(players[name])


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    players = {}
    for name in PLAYER_NAMES:
        players[name] = gen_player_achievements()
        print(f"Player {name}: {players[name]}")

    print(f"\nAll distinct achievements: {get_all_unique(players)}")
    print(f"Common achievements: {get_common_all(players)}\n")

    for name in PLAYER_NAMES:
        print(f"Only {name} has: {get_exclusive(name, players)}")

    print()

    for name in PLAYER_NAMES:
        print(f"{name} is missing: {get_missing(name, players)}")


if __name__ == "__main__":
    main()
