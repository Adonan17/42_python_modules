#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "r")
    except OSError as error:
        msg = f"[STDERR] Error opening file '{filename}': {error}\n"
        sys.stderr.write(msg)
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
        if line:
            new_line = line + "#\n"
            transformed.append(new_line)
            print(new_line, end="")

    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file = sys.stdin.readline().rstrip("\n")

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
            msg = f"[STDERR] Error opening file '{new_file}': {error}\n"
            sys.stderr.write(msg)
            print("Data not saved.")


if __name__ == "__main__":
    main()
