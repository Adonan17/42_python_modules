#!/usr/bin/env python3

import math


def calculate_distance(point1: tuple, point2: tuple) -> float:
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coord_str: str) -> tuple:
    try:
        parts = coord_str.split(",")
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return (x, y, z)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


def main():
    print("=== Game Coordinate System ===")

    position = (10, 20, 5)
    print(f"Position created: {position}")

    origin = (0, 0, 0)
    dist = calculate_distance(origin, position)
    print(f"Distance between {origin} and {position}: {dist:.2f}")

    coord_str = "3,4,0"
    print(f"\nParsing coordinates: \"{coord_str}\"")

    parsed = parse_coordinates(coord_str)
    print(f"Parsed position: {parsed}")
    dist = calculate_distance(origin, parsed)
    print(f"Distance from origin: {dist:.1f}")

    bad_str = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{bad_str}\"")

    parse_coordinates(bad_str)

    point = (3, 4, 0)
    x, y, z = point

    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
