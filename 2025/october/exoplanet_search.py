"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-05
                    Space Week Day 2: Exoplanet Search
For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical values:
Characters 0-9 correspond to luminosity levels 0-9.
Characters A-Z correspond to luminosity levels 10-35.
A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.
"""

def get_luminosity(ch):
    return int(ch) if ch.isdigit() else ord(ch)-ord('A') +10
def has_exoplanet(readings):

    n = len(readings)

    readings_sum = 0

    for ch in readings:
        readings_sum+=get_luminosity(ch)
    average = float(readings_sum) / n

    target = 0.8 * average

    for ch in readings:
        
        curr = get_luminosity(ch)
        
        if curr <= target:
            return True
    return False
