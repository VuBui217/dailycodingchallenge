"""
Docstring for 2026.february.2026_winter_game_day_10
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-15
                    2026 Winter Games Day 10: Alpine Skiing
Given a ski hill's vertical drop, horizontal distance, and type, determine the difficulty rating of the hill.

To determine the rating:

Calculate the steepness of the hill by taking the drop divided by the distance.
Then, calculate the adjusted steepness based on the hill type:
"Downhill" multiply steepness by 1.2
"Slalom": multiply steepness by 0.9
"Giant Slalom": multiply steepness by 1.0
Return:

"Green" if the adjusted steepness is less than or equal to 0.1
"Blue" if the adjusted steepness is greater than 0.1 and less than or equal to 0.25
"Black" if the adjusted steepness is greater than 0.25
"""
def get_hill_rating(drop, distance, hill_type):
    steepness_map = {"Downhill": 1.2, "Slalom": 0.9, "Giant Slalom": 1.0}
    steepness = (drop / distance) * steepness_map[hill_type]

    if steepness <= 0.1:
        return "Green"
    elif 0.1 < steepness <= 0.25:
        return  "Blue"
    else:
        return "Black"

print(get_hill_rating(95, 900, "Slalom")        )  # should return "Green".
print(get_hill_rating(620, 2800, "Downhill")    )  # should return "Black".
print(get_hill_rating(420, 1680, "Giant Slalom"))  # should return "Blue".
print(get_hill_rating(250, 3000, "Downhill")    )  # should return "Green".
print(get_hill_rating(110, 900, "Slalom")       )  # should return "Blue".
print(get_hill_rating(380, 1500, "Giant Slalom"))  # should return "Black".