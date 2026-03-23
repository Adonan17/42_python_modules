#!/usr/bin/env python3

import sys


def print_arguments(args: list) -> None:
    i = 0
    while i < len(args):
        print(f"Argument {i + 1}: {args[i]}")
        i += 1


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    args = sys.argv[1:]

    if len(args) == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args)}")
        print_arguments(args)

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
