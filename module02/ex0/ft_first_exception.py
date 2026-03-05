#!/usr/bin/env python3

def check_temperature(temp_str):
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")

def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    tests = ["25", "abc", "100", "-50"]

    for temp in tests:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)
        print()

    print("All tests completed. Program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()