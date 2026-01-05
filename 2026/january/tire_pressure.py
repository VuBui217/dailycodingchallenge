"""
Docstring for 2026.january.tire_pressure
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-05
                        Tire Pressure
Given an array with four numbers representing the tire pressures in psi of the four tires in your vehicle, and another array of two numbers representing the minimum and maximum pressure for your tires in bar, return an array of four strings describing each tire's status.

1 bar equal 14.5038 psi.
Return an array with the following values for each tire:

"Low" if the tire pressure is below the minimum allowed.
"Good" if it's between the minimum and maximum allowed.
"High" if it's above the maximum allowed.
"""
def tire_status(pressures_psi, range_bar):
    min_range = range_bar[0] * 14.5038
    max_range = range_bar[1] * 14.5038
    return [ "Low" if p < min_range else "High" if p > max_range else "Good" for p in pressures_psi ]

print(tire_status([32, 28, 35, 29], [2, 3])    )   # should return ["Good", "Low", "Good", "Low"].
print(tire_status([32, 28, 35, 30], [2, 2.3])  )   # should return ["Good", "Low", "High", "Good"].
print(tire_status([29, 26, 31, 28], [2.1, 2.5]))   # should return ["Low", "Low", "Good", "Low"].
print(tire_status([31, 31, 30, 29], [1.5, 2])  )   # should return ["High", "High", "High", "Good"].
print(tire_status([30, 28, 30, 29], [1.9, 2.1]))   # should return ["Good", "Good", "Good", "Good"].