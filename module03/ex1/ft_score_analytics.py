#!/usr/bin/env python3

import sys

print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print(
        "No scores provided. Usage: python3 ft_score_analytics.py "
        "<score1> <score2> ..."
    )
else:
    scores = []
    for i in range(1, len(sys.argv)):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError:
            print(
                f"Error: Invalid score '{sys.argv[i]}'. "
                "All scores must be integers."
                )
            sys.exit(1)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.2f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
