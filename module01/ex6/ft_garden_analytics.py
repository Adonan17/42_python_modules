#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days"

    def grow(self) -> None:
        self.height += 1
        self.age += 1


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int,
                 bloom_season: str) -> None:
        super().__init__(name, height, age)
        self.bloom_season = bloom_season

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, blooms in {self.bloom_season}"

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 bloom_season: str, prize_points: int) -> None:
        super().__init__(name, height, age, bloom_season)
        self.prize_points = prize_points

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.prize_points}"


class GardenManager:

    _total_gardens = 0

    class GardenStats:

        @staticmethod
        def calculate_average_height(plants: list) -> float:
            if not plants:
                return 0.0
            return sum(p.height for p in plants) / len(plants)

        @staticmethod
        def calculate_total_growth(plants: list) -> int:
            return sum(p.height for p in plants)

        @staticmethod
        def count_plant_types(plants: list) -> dict:
            counts = {
                "regular": 0,
                "flowering": 0,
                "prize": 0
            }
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    counts["prize"] += 1
                elif isinstance(plant, FloweringPlant):
                    counts["flowering"] += 1
                else:
                    counts["regular"] += 1
            return counts

    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name
        self.plants = []
        GardenManager._total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all(self) -> None:
        if not self.plants:
            return
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")

    def get_report(self) -> None:
        print(f"\n=== {self.owner_name}'s Garden Report ===")

        if not self.plants:
            print("No plants in garden yet")
            return

        print("Plants in garden:")
        for plant in self.plants:
            info = plant.get_info()
            if isinstance(plant, FloweringPlant):
                print(f"- {info}")
                if isinstance(plant, PrizeFlower):
                    print(f"  Prize points: {plant.prize_points}")
            else:
                print(f"- {info}")

        total = len(self.plants)
        growth = self.GardenStats.calculate_total_growth(self.plants)
        types = self.GardenStats.count_plant_types(self.plants)

        print(f"\nPlants added: {total}, Total growth: {growth}cm")
        type_str = (f"{types['regular']} regular, "
                    f"{types['flowering']} flowering, "
                    f"{types['prize']} prize flowers")
        print(f"Plant types: {type_str}")

    def get_score(self) -> int:
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score

    @classmethod
    def create_garden_network(cls, *owner_names: str) -> list:
        gardens = []
        for name in owner_names:
            gardens.append(cls(name))
        return gardens

    @classmethod
    def get_total_gardens(cls) -> int:
        return cls._total_gardens

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0 and height <= 10000

    @staticmethod
    def format_plant_list(plants: list) -> str:
        if not plants:
            return "No plants"
        return ", ".join(p.name for p in plants)


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")

    oak = Plant("Oak Tree", 101, 365)
    rose = FloweringPlant("Rose", 26, 30, "spring")
    sunflower = FloweringPlant("Sunflower", 51, 45, "summer")
    prize_rose = PrizeFlower("Prize Rose", 28, 35, "spring", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    alice.add_plant(prize_rose)

    alice.grow_all()

    alice.get_report()

    print(f"\nHeight validation test: "
          f"{GardenManager.validate_height(25)}")
    print(f"Garden score - Alice: {alice.get_score()}")

    print("\n--- Creating Garden Network ---")
    gardens = GardenManager.create_garden_network("Bob", "Carol")

    gardens[0].add_plant(Plant("Cactus", 15, 90))
    gardens[0].add_plant(
        PrizeFlower("Prize Tulip", 20, 25, "spring", 15)
    )

    print(f"\nGarden score - Bob: {gardens[0].get_score()}")
    gardens[0].get_report()

    print(f"\nTotal gardens managed: "
          f"{GardenManager.get_total_gardens()}")

    plant_list = GardenManager.format_plant_list(alice.plants)
    print(f"\nAlice's plants: {plant_list}")


if __name__ == "__main__":
    ft_garden_analytics()
