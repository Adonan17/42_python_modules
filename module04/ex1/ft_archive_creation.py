#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return

    print("---")
    content = file.read()
    lines = content.split("\n")
    for line in lines:
        if line != "":
            print(line)
    print("---")
    file.close()
    print(f"File '{filename}' closed.")

    print()
    print("Transform data:")
    print("---")

    transformed = []
    for line in lines:
        if line != "":
            new_line = line + "#\n"
            transformed.append(new_line)
            print(new_line, end="")

    print("---")

    new_file = input("Enter new file name (or empty): ")

    if new_file == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_file}'.")
        try:
            out = open(new_file, "w")
            for line in transformed:
                out.write(line)
            out.close()
            print(f"Data saved in file '{new_file}'.")
        except OSError as error:
            print(f"Error writing file '{new_file}': {error}")


if __name__ == "__main__":
    main()
