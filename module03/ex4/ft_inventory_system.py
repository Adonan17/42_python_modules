#!/usr/bin/env python3

import sys


def parse_inventory(raw_args: list) -> dict:
    inventory = dict()
    for arg in raw_args:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name = parts[0]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            quantity = int(parts[1])
            inventory.update({name: quantity})
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
    return inventory


def print_percentages(inventory: dict) -> None:
    total = sum(inventory.values())
    for item in inventory.keys():
        pct = (inventory[item] / total) * 100
        print(f"Item {item} represents {round(pct, 1)}%")


def get_most_abundant(inventory: dict) -> tuple:
    best_item = ""
    best_qty = -1
    for item in inventory.keys():
        qty = inventory[item]
        if best_qty == -1 or qty > best_qty:
            best_item = item
            best_qty = qty
    return (best_item, best_qty)


def get_least_abundant(inventory: dict) -> tuple:
    worst_item = ""
    worst_qty = -1
    for item in inventory.keys():
        qty = inventory[item]
        if worst_qty == -1 or qty < worst_qty:
            worst_item = item
            worst_qty = qty
    return (worst_item, worst_qty)


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory(sys.argv[1:])
    total = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: {total}")

    print_percentages(inventory)

    most_item, most_qty = get_most_abundant(inventory)
    least_item, least_qty = get_least_abundant(inventory)
    print(f"Item most abundant: {most_item} with quantity {most_qty}")
    print(f"Item least abundant: {least_item} with quantity {least_qty}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
