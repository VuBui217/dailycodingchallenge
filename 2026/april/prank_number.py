"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-01
                    Prank Number
Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't follow the pattern fixed.

The pattern will be one of:

The numbers increase from one to the next by a fixed amount (addition).
The numbers decrease from one to the next by a fixed amount (subtraction).
For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10].
"""
def fix_prank_number(arr):
    # Find the step
    diff_count = {}
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        diff_count[diff] = diff_count.get(diff, 0) + 1
    
    step = max(diff_count, key=diff_count.get)

    # Find the prank number and replace it with the right number
    res = arr[:]
    for i in range(1, len(res)):
        if res[i] - res[i-1] != step: 
            if i == len(res) - 1:
                # bad pair is the last pair
                res[i] = res[i-1] + step
            elif res[i+1] - res[i] != step:
                # next pair is also wrong, a[i] is prank
                res[i] = res[i-1] + step
            else:
                res[i-1] = res[i] - step
    
    return res

print(fix_prank_number([2, 4, 7, 8, 10])) # should return [2, 4, 6, 8, 10].
print(fix_prank_number([10, 10, 8, 7, 6])) # should return [10, 9, 8, 7, 6].
print(fix_prank_number([12, 24, 36, 48, 61, 72, 84, 96])) # should return [12, 24, 36, 48, 60, 72, 84, 96].
print(fix_prank_number([4, 1, -2, -5, -8, -5])) # should return [4, 1, -2, -5, -8, -11].
print(fix_prank_number([0, 100, 200, 300, 150, 500])) # should return [0, 100, 200, 300, 400, 500].
print(fix_prank_number([400, 425, 400, 375, 350, 325, 300])) # should return [450, 425, 400, 375, 350, 325, 300].
print(fix_prank_number([-5, 5, 10, 15, 20])) # should return [0, 5, 10, 15, 20].