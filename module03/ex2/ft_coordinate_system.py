#!/usr/bin/env python3

import math


def calculate_distance(point1: tuple, point2: tuple) -> float:
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt(
        (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    )


def get_player_pos() -> tuple:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        coords = []
        valid = True
        for part in parts:
            try:
                coords.append(float(part.strip()))
            except ValueError as e:
                print(f"Error on parameter '{part.strip()}': {e}")
                valid = False
                break
        if valid:
            return (coords[0], coords[1], coords[2])


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    x, y, z = pos1
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={x}, Y={y}, Z={z}")

    origin = (0.0, 0.0, 0.0)
    dist = calculate_distance(origin, pos1)
    print(f"Distance to center: {round(dist, 4)}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    dist = calculate_distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {round(dist, 4)}")


if __name__ == "__main__":
    main()
