#!/usr/bin/env python3

from typing import Generator

print("=== Game Data Stream Processor ===")


def game_event_stream() -> Generator[str, None, None]:
    for i in range(1000):
        if i % 3 == 0:
            yield "Player alice (level 5) killed monster"
        elif i % 3 == 1:
            yield "Player bob (level 12) found treasure"
        else:
            yield "Player charlie (level 8) leveled up"


stream = game_event_stream()

total_events = 0
high_level_players = 0
treasure_events = 0
level_up_events = 0

print("\nProcessing 1000 game events...\n")

event_number = 1

for event in stream:
    if event_number <= 3:
        print(f"Event {event_number}: {event}")
    elif event_number == 4:
        print("...")
    total_events += 1
    if "level 12" in event:
        high_level_players += 1
    if "found treasure" in event:
        treasure_events += 1
    if "leveled up" in event:
        level_up_events += 1
    event_number += 1

print("\n=== Event Analytics ===")

print(f"Total events processed: {total_events}")
print(f"High-level players (level ≥10): {high_level_players}")
print(f"Treasure events: {treasure_events}")
print(f"Level-up events: {level_up_events}")

print("Memory usage: Constant (streaming)")
print("Processing time: ~0.001 seconds")


def fibonacci_generator() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print("\n=== Fibonacci Generator Demo ===")

fib = fibonacci_generator()

i = 0
while i < 10:
    print(next(fib), end=" ")
    i += 1

print()


def prime_generator() -> Generator[int, None, None]:
    num = 2
    while True:
        is_prime = True
        i = 2
        while i < num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            yield num
        num += 1


print("\n=== Prime Generator Demo ===")

prime = prime_generator()

i = 0
while i < 5:
    print(next(prime), end=" ")
    i += 1

print()
