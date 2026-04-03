#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        file = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
    else:
        print("---")
        content = file.read()
        print(content, end="")
        file.close()
        print()
        print("---")
        print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
