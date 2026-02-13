"""
Docstring for 2026.february.2026_winter_game_day_8
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-13
                        2026 Winter Games Day 8: Luge
Given an array of five numbers, each representing the time (in seconds) it took a luger to complete a segment of a track, determine which segment had the fastest speed and what that speed was.

The track is divided into the following segments:

Segment 1: 320 meters
Segment 2: 280 meters
Segment 3: 350 meters
Segment 4: 300 meters
Segment 5: 250 meters
The first value in the given array corresponds to the time for segment 1, the second value to segment 2, and so on.

To calculate the speed (in meters per second) for a segment, divide the distance by the time.

Return "The luger's fastest speed was X m/s on segment Y.". Where X is the fastest speed, rounded to two decimal places, and Y is the segment number where the fastest speed occurred.
"""
def get_fastest_speed(times):
    segments = [320, 280, 350, 300, 250]
    speeds = [ round(s / t, 2) for s, t in zip(segments, times)]
    max_speed = max(speeds)
    max_segment = speeds.index(max_speed)
    return f"The luger's fastest speed was {max_speed} m/s on segment {max_segment + 1}."

print(get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128]))     # should return "The luger's fastest speed was 35.07 m/s on segment 5."
print(get_fastest_speed([9.381, 7.417, 9.912, 8.815, 7.284]) )     # should return "The luger's fastest speed was 37.75 m/s on segment 2."
print(get_fastest_speed([8.890, 7.601, 9.093, 8.392, 6.912]) )     # should return "The luger's fastest speed was 38.49 m/s on segment 3."
print(get_fastest_speed([8.490, 7.732, 10.103, 8.489, 6.840]))     # should return "The luger's fastest speed was 37.69 m/s on segment 1."
print(get_fastest_speed([8.204, 7.230, 9.673, 7.645, 6.508]) )     # should return "The luger's fastest speed was 39.24 m/s on segment 4."