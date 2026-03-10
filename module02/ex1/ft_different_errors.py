#!/usr/bin/env python3


def garden_operations(operation: str) -> None:
    if operation == "value":
        int("abc")
    elif operation == "zero":
        10 / 0
    elif operation == "file":
        f = open("missing.txt")
        f.close()
    elif operation == "key":
        plants = {"rose": 1}
        print(plants["missing_plant"])


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print()

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print()

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()

    print("Testing multiple errors together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")
    print()

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
