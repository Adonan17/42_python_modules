#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def get_info(self):
        base_info = super().get_info()
        return f"{self.name} (Flower): {base_info}, {self.color} color"

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self):
        base_info = super().get_info()
        return (
            f"{self.name} (Tree): {base_info}, "
            f"{self.trunk_diameter}cm diameter"
        )

    def produce_shade(self):
        shade = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        base_info = super().get_info()
        return (
            f"{self.name} (Vegetable): {base_info}, "
            f"{self.harvest_season} harvest"
        )

    def nutri_value(self):
        print(f"{self.name} is rich in {self.nutritional_value}!")


def ft_plant_types():
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print("=== Garden Plant Types ===")
    print()
    print(rose.get_info())
    rose.bloom()
    print()
    print(oak.get_info())
    oak.produce_shade()
    print()
    print(tomato.get_info())
    tomato.nutri_value()
    print()
    lily = Flower("Lily", 20, 15, "white")
    print(lily.get_info())
    lily.bloom()
    print()
    pine = Tree("Pine", 300, 1200, 40)
    print(pine.get_info())
    pine.produce_shade()
    print()
    carrot = Vegetable("Carrot", 30, 70, "autumn", "vitamin A")
    print(carrot.get_info())
    carrot.nutri_value()


if __name__ == "__main__":
    ft_plant_types()
