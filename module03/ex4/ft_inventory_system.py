#!/usr/bin/env python3

import sys

print("=== Inventory System Analysis ===")

inventory = dict()
i = 1
while i < len(sys.argv):
    parts = sys.argv[i].split(":")
    item_name = parts[0]
    quantity = int(parts[1])
    inventory.update({item_name: quantity})
    i += 1

total_items = 0
for value in inventory.values():
    total_items += value

unique_types = len(inventory)

print(f"Total items in inventory: {total_items}")
print(f"Unique item types: {unique_types}")

print("\n=== Current Inventory ===")
for item, quantity in inventory.items():
    percentage = (quantity / total_items) * 100
    if quantity == 1:
        print(f"{item}: {quantity} unit ({percentage:.1f}%)")
    else:
        print(f"{item}: {quantity} units ({percentage:.1f}%)")


print("\n=== Inventory Statistics ===")

most_item = ""
most_quantity = -1
least_item = ""
least_quantity = -1

for item, quantity in inventory.items():
    if most_quantity == -1 or quantity > most_quantity:
        most_item = item
        most_quantity = quantity

    if least_quantity == -1 or quantity < least_quantity:
        least_item = item
        least_quantity = quantity

print(f"Most abundant: {most_item} ({most_quantity} units)")
print(f"Least abundant: {least_item} ({least_quantity} units)")

print("\n=== Item Categories ===")

categories = dict()
categories.update({"abundant": dict()})
categories.update({"moderate": dict()})
categories.update({"scarce": dict()})

for item, quantity in inventory.items():
    if quantity >= 6:
        categories["abundant"].update({item: quantity})
    elif quantity >= 4:
        categories["moderate"].update({item: quantity})
    else:
        categories["scarce"].update({item: quantity})

print(f"Abundant: {categories['abundant']}")
print(f"Moderate: {categories['moderate']}")
print(f"Scarce: {categories['scarce']}")

print("\n=== Management Suggestions ===")

restock = ""

for item, quantity in inventory.items():
    if quantity <= 1:
        if restock == "":
            restock = item
        else:
            restock += ", " + item

print(f"Restock needed: {restock}")

print("\n=== Dictionary Properties Demo ===")

keys_text = ""
for key in inventory.keys():
    if keys_text == "":
        keys_text = key
    else:
        keys_text += ", " + key

print(f"Dictionary keys: {keys_text}")

values_text = ""
for value in inventory.values():
    if values_text == "":
        values_text = str(value)
    else:
        values_text += ", " + str(value)

print(f"Dictionary values: {values_text}")

print(
    f"Sample lookup - 'sword' in inventory: "
    f"{inventory.get('sword') is not None}"
)
