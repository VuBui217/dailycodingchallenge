"""
Docstring for 2026.february.2026_winter_game_day_2
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-07
                    2026 Winter Games Day 2: Snowboarding
Given a snowboarder's starting stance and a rotation in degrees, determine their landing stance.

A snowboarder's stance is either "Regular" or "Goofy".
Trick rotations are multiples of 90 degrees. Positive indicates clockwise rotation, and negative indicate counter-clockwise rotation.
The landing stance flips every 180 degrees of rotation.
For example, given "Regular" and 90, return "Regular". Given "Regular" and 180 degrees, return "Goofy".
"""

def get_landing_stance(start_stance, rotation):
    flip = abs(rotation) // 180

    if flip % 2 == 1:
        return "Regular" if start_stance == "Goofy" else "Goofy"

    return start_stance
    
print(get_landing_stance("Regular", 90)  ) # should return "Regular".
print(get_landing_stance("Regular", 180) ) # should return "Goofy".
print(get_landing_stance("Goofy", -270)  ) # should return "Regular".
print(get_landing_stance("Regular", 2340)) # should return "Goofy".
print(get_landing_stance("Goofy", 2160)  ) # should return "Goofy".