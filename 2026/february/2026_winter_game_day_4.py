"""
Docstring for 2026.february.2026_winter_game_day_4
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-09
2026 Winter Games Day 4: Ski Jumping
Given distance points, style points, a wind compensation value, and K-point bonus value, calculate your score for the ski jump and determine if you won a medal or not.

Your score is calculated by summing the above four values.
The current total scores of the other jumpers are:

165.5
172.0
158.0
180.0
169.5
175.0
162.0
170.0
If your score is the best, return "Gold"
If it's second best, return "Silver"
If it's third best, return "Bronze"
Otherwise, return "No Medal"
"""
def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    total = distance_points + style_points + wind_comp + k_point_bonus
    scores = [165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0]
    scores.append(total)
    scores.sort(reverse=True)
    rank = scores.index(total)
    if rank == 0:
        return "Gold"
    elif rank == 1:
        return "Silver"
    elif rank == 2:
        return  "Bronze"
    else:
        return "No Medal"

print(ski_jump_medal(125.0, 58.0, 0.0, 6.0) )  # should return "Gold".
print(ski_jump_medal(119.0, 50.0, 1.0, 4.0) )  # should return "Bronze".
print(ski_jump_medal(122.0, 52.0, -1.0, 4.0))  # should return "Silver".
print(ski_jump_medal(118.0, 50.5, -1.5, 4.0))  # should return "No Medal".
print(ski_jump_medal(124.0, 50.5, 2.0, 5.0) )  # should return "Gold".
print(ski_jump_medal(119.0, 49.5, 0.0, 3.0) )  # should return "No Medal".