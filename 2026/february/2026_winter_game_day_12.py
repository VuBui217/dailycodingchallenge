"""
Docstring for 2026.february.2026_winter_game_day_12
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-17
                        2026 Winter Games Day 12: Bobsled
Given an array representing the weights of the athletes on a bobsled team and a number representing the weight of the bobsled, determine whether the team is eligible to race.

The length of the array determines the team size: 1, 2 or 4 person teams.
All given weight values are in kilograms (kg).
The bobsled (sled by iteself) must have a minimum weight of:

162 kg for a 1-person team
170 kg for a 2-person team
210 kg for a 4-person team
The total weight of the bobsled (athletes plus sled) must not exceed:

247 kg for a 1-person team
390 kg for a 2-person team
630 kg for a 4-person team
Return "Eligible" if the team meets all the requirements, or "Not Eligible" if the team fails to meet one or more of the requirements.
"""
def check_eligibility(athlete_weights, sled_weight):
    bobsled_map = {1: (162, 247), 2: (170, 390), 4: (210, 630)}
    team_count = len(athlete_weights)
    if sled_weight < bobsled_map[team_count][0]:
        return "Not Eligible"
    total_weight = sum(athlete_weights) + sled_weight
    if total_weight > bobsled_map[team_count][1]:
        return "Not Eligible"
    
    return "Eligible"
print(check_eligibility([78], 165)               ) # should return "Eligible".
print(check_eligibility([80], 160)               ) # should return "Not Eligible".
print(check_eligibility([80], 170)               ) # should return "Not Eligible".
print(check_eligibility([85, 90], 170)           ) # should return "Eligible".
print(check_eligibility([85, 95], 168)           ) # should return "Not Eligible".
print(check_eligibility([112, 97], 185)          ) # should return "Not Eligible".
print(check_eligibility([110, 102, 90, 106], 222)) # should return "Eligible".
print(check_eligibility([106, 99, 90, 88], 205)  ) # should return "Not Eligible".
print(check_eligibility([106, 99, 103, 96], 227) ) # should return "Not Eligible".