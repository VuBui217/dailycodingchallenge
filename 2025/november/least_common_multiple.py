"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-21

                                    LCM
Given two integers, return the least common multiple (LCM) of the two numbers.

The LCM of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given 4 and 6, return 12 because:

Multiples of 4 are 4, 8, 12 and so on.
Multplies of 6 are 6, 12, 18 and so on.
12 is the smallest number that is a multiple of both.s
"""
def lcm(a, b):
    # output = 0
    # i = 1
    # while True:
    #     output = max(a, b) * i
    #     if output % min(a, b) == 0:
    #         return output
    #     i += 1

    # Use this formula:
    # lcm(a, b) = abs(axb) // gcd(a, b)

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    return abs(a * b) // gcd(a, b)

lcm(4, 6)       #should return 12.
lcm(9, 6)       #should return 18.
lcm(10, 100)    #should return 100.
lcm(13, 17)     #should return 221.
lcm(45, 70)     #should return 630.
    