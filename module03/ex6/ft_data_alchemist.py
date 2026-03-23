#!/usr/bin/env python3

import random


INITIAL_PLAYERS = [
    "Alice", "bob", "Charlie", "dylan", "Emma",
    "Gregory", "john", "kevin", "Liam",
]


def build_score_dict(players: list) -> dict:
    return {player: random.randint(1, 1000) for player in players}


def get_high_scores(scores: dict, average: float) -> dict:
    return {
        player: score
        for player, score in scores.items()
        if score > average
    }


def main() -> None:
    print("=== Game Data Alchemist ===")

    all_capitalized = [name.capitalize() for name in INITIAL_PLAYERS]
    already_capitalized = [
        name for name in INITIAL_PLAYERS if name[0].isupper()
    ]

    print(f"Initial list of players: {INITIAL_PLAYERS}")
    print(f"New list with all names capitalized: {all_capitalized}")
    print(f"New list of capitalized names only: {already_capitalized}")

    score_dict = build_score_dict(all_capitalized)
    print(f"Score dict: {score_dict}")

    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average, 2)}")

    high_scores = get_high_scores(score_dict, average)
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
