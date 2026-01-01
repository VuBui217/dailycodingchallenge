"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-01

                    Miles to Kilometers
Given a distance in miles as a number, return the equivalent distance in kilometers.

The input will always be a non-negative number.
1 mile equals 1.60934 kilometers.
Round the result to two decimal places.
"""
def convert_to_km(miles):
    miles_in_kilometers = round(miles * 1.60934, 2)
    return miles_in_kilometers

print(f"{1.60934:.2f}")
print(convert_to_km(21))

convert_to_km(1)        # should return 1.61.
convert_to_km(21)       # should return 33.8.
convert_to_km(3.5)      # should return 5.63.
convert_to_km(0)        # should return 0.
convert_to_km(0.621371) # should return 1.