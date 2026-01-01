"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-06

Space Week Day 3: Phone Home
For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:

The first value in the array is the distance from your location to the first satellite.
Each subsequent value, except for the last, is the distance to the next satellite.
The last value in the array is the distance from the previous satellite to your home planet.
The message travels at 300,000 km/s.
Each satellite the message passes through adds a 0.5 second transmission delay.
Return a number rounded to 4 decimal places, with trailing zeros removed.
"""

def send_message(route):
    n = len(route) 
    # number of satellites
    num_satellites = n-1
    # total delay time of n-1 satellites
    t_delay = 0.5 * num_satellites
    # calculate to the total distance
    total_distance = sum(route)
    
    total_time = total_distance/300000 + t_delay

    return float(f"{total_time:.4f}")

print(send_message([300000, 300000]))
print(send_message([384400, 384400]))