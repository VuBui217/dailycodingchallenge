"""
Docstring for december.takeoff_fuel
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-29
                            Takeoff Fuel
Given the numbers of gallons of fuel currently in your airplane, and the required number of liters of fuel to reach your destination, determine how many additional gallons of fuel you should add.

1 gallon equals 3.78541 liters.
If the airplane already has enough fuel, return 0.
You can only add whole gallons.
Do not include decimals in the return number.
"""
def fuel_to_add(current_gallons, required_liters):
    import math
    diff = current_gallons * 3.78541 - required_liters

    return 0 if diff >= 0 else math.ceil(abs(diff) /  3.78541)
print(fuel_to_add(0, 1)       )    #should return 1.
print(fuel_to_add(5, 40)      )    #should return 6.
print(fuel_to_add(10, 30)     )    #should return 0.
print(fuel_to_add(896, 20500) )    #should return 4520.
print(fuel_to_add(1000, 50000))    #should return 12209.