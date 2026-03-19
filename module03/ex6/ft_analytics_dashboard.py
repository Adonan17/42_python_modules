#!/usr/bin/env python3

print("=== Game Analytics Dashboard ===")

players = ["alice", "bob", "charlie", "diana"]

scores = [2300, 1700, 2150, 2000]

achievements = {
    "alice": [
        "first_kill", "level_10", "boss_slayer",
        "explorer", "collector"
    ],
    "bob": ["first_kill", "level_10", "collector"],
    "charlie": ["first_kill", "level_10", "boss_slayer", "explorer",
                "collector", "champion", "legend"],
    "diana": ["first_kill"]
}

regions = ["north", "east", "north", "central", "east"]

print("\n=== List Comprehension Examples ===")

high_scorers = [
    players[i] for i in range(len(players))
    if scores[i] > 2000
]
print(f"High scorers (>2000): {high_scorers}")

doubled_scores = [score * 2 for score in scores]
print(f"Scores doubled: {doubled_scores}")

active_players = [
    players[i] for i in range(len(players))
    if scores[i] >= 1800
]
print(f"Active players: {active_players}")

print("\n=== Dict Comprehension Examples ===")

player_scores = {
    players[i]: scores[i]
    for i in range(len(players))
}
print(f"Player scores: {player_scores}")

score_categories = {
    "high": len([s for s in scores if s >= 2000]),
    "medium": len([s for s in scores if 1800 <= s < 2000]),
    "low": len([s for s in scores if s < 1800])
}
print(f"Score categories: {score_categories}")

achievement_counts = {
    player: len(achievements[player])
    for player in achievements
}
print(f"Achievement counts: {achievement_counts}")

print("\n=== Set Comprehension Examples ===")

unique_players = {player for player in players}
print(f"Unique players: {unique_players}")

unique_achievements = {
    achievement
    for player in achievements
    for achievement in achievements[player]
}
print(f"Unique achievements: {unique_achievements}")

unique_regions = {region for region in regions}
print(f"Active regions: {unique_regions}")

print("\n=== Combined Analysis ===")

print(f"Total players: {len(players)}")
print(f"Total unique achievements: {len(unique_achievements)}")

average_score = sum(scores) / len(scores)
print(f"Average score: {average_score}")

max_score = max(scores)

i = 0
while i < len(players):
    if scores[i] == max_score:
        top_player = players[i]
        break
    i += 1

print(
    f"Top performer: {top_player} "
    f"({max_score} points, {achievement_counts[top_player]} achievements)"
)
