#!/usr/bin/env python3

print("=== Achievement Tracker System ===")
print()
alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
bob = {"first_kill", "level_10", "boss_slayer", "collector"}
charlie = {"level_10", "treasure_hunter", "boss_slayer",
           "speed_demon", "perfectionist"}
print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

print("\n=== Achievement Analytics ===")

all_achievements = alice.union(bob).union(charlie)
print(f"All unique achievements: {all_achievements}")
print(f"Total unique achievements: {len(all_achievements)}")

common_all = alice.intersection(bob).intersection(charlie)
print(f"\nCommon to all players: {common_all}")

alice_only = alice.difference(bob.union(charlie))
bob_only = bob.difference(alice.union(charlie))
charlie_only = charlie.difference(alice.union(bob))
rare = alice_only.union(bob_only).union(charlie_only)
print(f"Rare achievements (1 player): {rare}")

alice_bob_common = alice.intersection(bob)
alice_unique = alice.difference(bob)
bob_unique = bob.difference(alice)

print(f"\nAlice vs Bob common: {alice_bob_common}")
print(f"Alice unique: {alice_unique}")
print(f"Bob unique: {bob_unique}")
