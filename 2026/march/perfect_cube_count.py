"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-03
                    Perfect Cube Count
Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

The lower number is not garanteed to be the first argument.
A number is a perfect cube if there exists an integer (n) where n * n * n = number. For example, 27 is a perfect cube because 3 * 3 * 3 = 27.
"""
def count_perfect_cubes(a, b):
    start = min(a, b)
    end = max(a, b)
    # Solution 1: Check every num in the range --> O(n)
    # count = 0

    # for num in range(start, end + 1):
    #     if num < 0:
    #         cube_root = -round((-num) ** (1/3))
    #     else:
    #         cube_root = round(num ** (1/3))
    #     if num == cube_root ** 3:
    #         count += 1
    # return count

    # Solution 2: Find the first and last integer whose cube falls in the range, then subtract
    import math
    def cbrt(num):
        return -((-num) ** (1/3)) if num < 0 else (num ** (1/3))
    
    min_cube = math.ceil(cbrt(start) - 1e-9)
    max_cube = math.floor(cbrt(end) + 1e-9)

    return max(0, max_cube - min_cube + 1)

print(count_perfect_cubes(3, 30))          # should return 2.
print(count_perfect_cubes(1, 30))          # should return 3.
print(count_perfect_cubes(30, 0))          # should return 4.
print(count_perfect_cubes(-64, 64))        # should return 9.
print(count_perfect_cubes(9214, -8127))    # should return 41.
