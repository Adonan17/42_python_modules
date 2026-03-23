#!/usr/bin/env python3

import random
from typing import Generator


PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb", "swim",
           "use", "release", "jump"]


def gen_event() -> Generator[tuple, None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(events: list) -> Generator[tuple, None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        event = events[index]
        events.pop(index)
        yield event


def display_thousand_events() -> None:
    generator = gen_event()
    for i in range(1000):
        name, action = next(generator)
        print(f"Event {i}: Player {name} did action {action}")


def build_event_list(count: int) -> list:
    generator = gen_event()
    events = []
    for _ in range(count):
        events.append(next(generator))
    return events


def consume_and_display(events: list) -> None:
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


def main() -> None:
    print("=== Game Data Stream Processor ===")
    display_thousand_events()
    events = build_event_list(10)
    consume_and_display(events)


if __name__ == "__main__":
    main()
