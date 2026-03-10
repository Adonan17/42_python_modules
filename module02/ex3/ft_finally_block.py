#!/usr/bin/env python3


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()

    good_plants = ["tomato", "lettuce", "carrots"]
    bad_plants = ["tomato", None, "carrots"]

    print("Testing normal watering...")
    water_plants(good_plants)
    print("Watering completed successfully!")
    print()

    print("Testing with error...")
    water_plants(bad_plants)
    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
