#!/usr/bin/env python3


class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self._initial_height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def report_line(self):
        return f"{self.name}: {self.height}cm"

    def prize_line(self):
        return None

    def kind(self):
        return "plant"

    def growth(self):
        return self.height - self._initial_height

    def prize_points_value(self):
        return 0


class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color, blooming_status):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.blooming_status = blooming_status

    def report_line(self):
        base = super().report_line()
        return (
            f"{base}, {self.flower_color} flowers "
            f"({self.blooming_status})"
        )

    def kind(self):
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name,
        height,
        flower_color,
        blooming_status,
        prize_points,
    ):
        super().__init__(name, height, flower_color, blooming_status)
        self.prize_points = prize_points

    def prize_line(self):
        return f"Prize points: {self.prize_points}"

    def kind(self):
        return "prize"

    def prize_points_value(self):
        return self.prize_points


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants = self.plants + [plant]
        print(
            f"{self.owner} added {plant.name} "
            f"to her garden"
        )

    def grow_all(self):
        print(
            f"{self.owner} is helping "
            f"all plants grow..."
        )
        for plant in self.plants:
            plant.grow()

    def report(self):
        print(f"--- {self.owner}'s Garden Report ---")

        count = 0
        for plant in self.plants:
            print(plant.report_line())
            extra = plant.prize_line()
            if extra is not None:
                print(extra)
            count += 1

        print(f"Total plants: {count}")

    def plants_count(self):
        count = 0
        for _ in self.plants:
            count += 1
        return count


class GardenManager:
    gardens_managed = 0

    def __init__(self):
        self.gardens = []

    def add_garden(self, garden):
        self.gardens = self.gardens + [garden]
        GardenManager.gardens_managed += 1

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def total_height(self):
            total = 0
            for plant in self.garden.plants:
                total += plant.height
            return total

        def total_growth(self):
            total = 0
            for plant in self.garden.plants:
                total += plant.growth()
            return total

        def total_prize_points(self):
            total = 0
            for plant in self.garden.plants:
                total += plant.prize_points_value()
            return total

        def count_by_kind(self):
            regular = 0
            flowering = 0
            prize = 0

            for plant in self.garden.plants:
                kind = plant.kind()
                if kind == "plant":
                    regular += 1
                elif kind == "flowering":
                    flowering += 1
                elif kind == "prize":
                    prize += 1

            return regular, flowering, prize

        def score(self):
            base = self.total_height()
            prize_points = self.total_prize_points()
            growth_bonus = self.total_growth() * 10
            return base + prize_points + growth_bonus

    @staticmethod
    def validate_height(height):
        return height >= 0

    @classmethod
    def create_garden_network(cls, gardens):
        scores = {}
        for garden in gardens:
            stats = cls.GardenStats(garden)
            scores[garden.owner] = stats.score()

        print(
            f"Garden scores - Alice: {scores['Alice']}, "
            f"Bob: {scores['Bob']}"
        )
        return scores


def ft_garden_analytics():
    print("=== Garden Analytics System ===")

    manager = GardenManager()

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", "blooming")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", "blooming", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.grow_all()

    print()
    alice_garden.report()

    print()
    print(f"Height validation test: {GardenManager.validate_height(10)}")

    manager.create_garden_network([alice_garden, bob_garden])

    print(f"Total gardens managed: {GardenManager.gardens_managed}")


if __name__ == "__main__":
    ft_garden_analytics()
