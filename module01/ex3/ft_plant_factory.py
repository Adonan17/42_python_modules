#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def plant_factory():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
    print("\nTotal plants created: 5")


if __name__ == "__main__":
    plant_factory()
