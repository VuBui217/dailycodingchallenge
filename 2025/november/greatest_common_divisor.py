"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-15

                                GCD
Given two positive integers, return their greatest common divisor (GCD).

The GCD of two integers is the largest number that divides evenly into both numbers without leaving a remainder.
For example, the divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3, and 6. So given 4 and 6, return 2, the largest number that appears in both sets of divisors.
"""
def gcd(x, y):

    #The Euclidean algorithm is an efficient method for computing the GCD.
    while y != 0:
        
        x, y = y, x % y #swapping
    return x

gcd(4, 6)       #should return 2.
gcd(20, 15)     #should return 5.
gcd(13, 17)     #should return 1.
gcd(654, 456)   #should return 6.
gcd(3456, 4320) #should return 864.