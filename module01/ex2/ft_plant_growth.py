#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def increase_age(self):
        self.age += 1

    def get_info(self):
        return (f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    starting_heights = [
        plants[0].height,
        plants[1].height,
        plants[2].height,
    ]

    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    for i in range(6):
        for plant in plants:
            plant.grow()
            plant.increase_age()

    print("=== Day 7 ===")
    for i in range(3):
        print(plants[i].get_info())
        print(f"Growth this week: +{plants[i].height - starting_heights[i]}cm")


if __name__ == "__main__":
    ft_plant_growth()
