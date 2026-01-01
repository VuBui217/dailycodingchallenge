"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-04

Space Week Day 1: Stellar Classification
October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.

For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar classification based on the following ranges:

"O": 30,000 K or higher
"B": 10,000 K - 29,999 K
"A": 7,500 K - 9,999 K
"F": 6,000 K - 7,499 K
"G": 5,200 K - 5,999 K
"K": 3,700 K - 5,199 K
"M": 0 K - 3,699 K
Return the classification of the given star.
"""

def classification(temp):

    if temp >= 30000:
        return 'O'
    elif 29999>= temp >= 10000:
        return 'B'
    elif 9999>= temp >= 7500:
        return 'A'
    elif 7499>= temp >= 6000:
        return 'F'
    elif 5999>= temp >= 5200:
        return 'G'
    elif 5199>= temp >= 3700:
        return 'K'
    elif 3699>= temp >=0:
        return 'M'
    else:
        return 'Invalid temperature'

print(classification(5778)  )    #should return "G".
print(classification(2400)  )    #should return "M".
print(classification(9999)  )    #should return "A".
print(classification(3700)  )    #should return "K".
print(classification(3699)  )    #should return "M".
print(classification(210000))    #should return "O".
print(classification(6000)  )    #should return "F".
print(classification(11432) )    #should return "B".