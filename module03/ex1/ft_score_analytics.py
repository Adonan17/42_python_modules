#!/usr/bin/env python3

import sys


def parse_scores(raw_args: list) -> list:
    scores = []
    for arg in raw_args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores


def print_usage() -> None:
    print(
        "No scores provided. Usage: python3 ft_score_analytics.py "
        "<score1> <score2> ..."
    )


def print_analytics(scores: list) -> None:
    total = sum(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {total / len(scores):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def main() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print_usage()
        return

    scores = parse_scores(sys.argv[1:])

    if len(scores) == 0:
        print_usage()
        return

    print_analytics(scores)


if __name__ == "__main__":
    main()
