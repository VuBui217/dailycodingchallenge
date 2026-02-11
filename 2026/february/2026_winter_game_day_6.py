"""
Docstring for 2026.february.2026_winter_game_day_6
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-11
                    2026 Winter Games Day 6: Figure Skating
Given an array of judge scores and optional penalties, calculate the final score for a figure skating routine.

The first argument is an array of 10 judge scores, each a number from 0 to 10. Remove the highest and lowest judge scores and sum the remaining 8 scores to get the base score.

Any additional arguments passed to the function are penalties. Subtract all penalties from the base score to get the final score.
"""
def compute_score(judge_scores, *penalties):
    max_score = max(judge_scores)
    min_score = min(judge_scores)
    base_score = sum(judge_scores) - (min_score + max_score)

    final_score = base_score - sum(penalties)
    return final_score
print(compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1)                               )    # should return 64.
print(compute_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])                         )    # should return 80.
print(compute_score([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1)                       )    # should return 67.
print(compute_score([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], 0.5, 1.0)     )    # should return 67.5.
print(compute_score([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], 1.5, 0.5, 0.5))    # should return 59.