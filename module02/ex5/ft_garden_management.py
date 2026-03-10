#!/usr/bin/env python3


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name):
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        self.plants = self.plants + [plant_name]

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        if plant_name == "":
            raise ValueError("Plant name cannot be empty!")

        if water_level < 1:
            raise ValueError(
                f"Water level {water_level} is too low (min 1)"
            )
        if water_level > 10:
            raise ValueError(
                f"Water level {water_level} is too high (max 10)"
            )

        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )

        return (
            f"{plant_name}: healthy (water: {water_level}, "
            f"sun: {sunlight_hours})"
        )


def test_garden_management():
    manager = GardenManager()

    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        print("Added tomato successfully")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("lettuce")
        print("Added lettuce successfully")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("")
        print("Added successfully")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print()
    print("Watering plants...")
    manager.water_plants()

    print()
    print("Checking plant health...")
    try:
        print(manager.check_plant_health("tomato", 5, 8))
    except ValueError as e:
        print(f"Error checking tomato: {e}")

    try:
        print(manager.check_plant_health("lettuce", 15, 8))
    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    print()
    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()