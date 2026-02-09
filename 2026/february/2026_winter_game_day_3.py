"""
Docstring for 2026.february.2026_winter_game_day_3
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-08
                    2026 Winter Games Day 3: Biathlon
Given an array of integers, where each value represents the number of targets hit in a single round of a biathlon, return the total penalty distance the athlete must ski.

Each round consists of 5 targets.
Each missed target results in a 150 meter penalty loop.
"""
def calculate_penalty_distance(rounds):
    return sum( max(0, (5 - curr)) * 150 for curr in rounds)

print(calculate_penalty_distance([4, 4])      )    # should return 300.
print(calculate_penalty_distance([5, 5])      )    # should return 0.
print(calculate_penalty_distance([4, 5, 3, 5]))    # should return 450.
print(calculate_penalty_distance([5, 4, 5, 5]))    # should return 150.
print(calculate_penalty_distance([4, 3, 0, 3]))    # should return 1500.