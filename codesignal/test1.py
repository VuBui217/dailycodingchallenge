"""
Problem 1
"""
def problem1_solution1(text: str) -> int:
    """Count words whose first and last characters match (case-insensitive)."""
    count = 0
    start = 0
    text += " "  # sentinel space so the final word is evaluated

    for idx, char in enumerate(text):
        if char == " ":
            # Skip consecutive spaces (empty words)
            if idx > start:
                first = text[start]
                last = text[idx - 1]
                if first.lower() == last.lower():
                    count += 1
            start = idx + 1

    return count

def problem1_solution2(strs):
    count = 0
    lst = strs.split(' ')

    for s in lst:
        if s[0].lower() == s[-1].lower():
            count+=1
    return count
# sample = "L0dfdfdfl world BoB" 
# print(problem1_solution1(sample))
# print(problem1_solution2(sample))

"""
problem 4
Given:
An array nums and a number threshold.
Goal:
Find the longest subarray such that
sum(subarray) - sum(interval before subarray) <= threshold.
"""
# O(n^2) 
def problem3(nums, threshold):
    n = len(nums)
    prefix = 0
    max_len = 0
    for l in range(n):
        curr = 0
        for r in range(l, n):
            curr+=nums[r]
            if curr - prefix <= threshold:
                max_len = max(max_len, r - l + 1)
        prefix+=nums[l]
    return max_len
# O(n^2)
def problem3_sol2(nums, threshold):
    n = len(nums)
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    
    max_len = 0
    for l in range(n):
        for r in range(l, n):
            if prefix[r+1] - 2*prefix[l] <= threshold:
                max_len = max(max_len, r - l + 1)
    return max_len
nums = [3,1,2,1,4]
print(problem3(nums, 5))

"""
Problem 4: Matrix
"""

def get_average(neighbors):
    return sum(neighbors)//len(neighbors)

def problem4_solution(matrix, radius):
    """
    Update each cell in the matrix by averaging its value with the mean of its neighbors within a given radius.

    Parameters:
        matrix (list of list of int): The input 2D matrix of integers.
        radius (int): The radius to consider for neighboring cells.

    Returns:
        list of list of int: The updated matrix after applying the averaging operation.
    """

    m, n = len(matrix), len(matrix[0]) # m rows, n columns

    updated_matrix = [[0 for _ in range(n)] for _ in range(m)] 

    for i in range(m):
        for j in range(n):
            neighbors = []

            for x in range(i-radius, i+radius+1):
                for y in range(j-radius, j+radius+1):
                    if 0 <= x < m and 0 <= y < n and not (x==i and y ==j):
                        neighbors.append(matrix[x][y])
            
            neighbors_mean = get_average(neighbors) if neighbors else 0
            updated_matrix[i][j] = (neighbors_mean+matrix[i][j]) //2

    return updated_matrix


# import requests
# import mysql.connector
# import pandas as pd

from collections import deque

"""
For dataSizes = [8, 5, 7, 1, 4, 1, 9] and threshold = 5, the output should be solution(dataSizes, threshold) = 4.

(5, 7, 1) -> 5 + 7 + 1 - 8 = 8 + 5 + 7 + 1 - 8 - 8

Explanation:
The contiguous subarray [6, 1, 4, 1] has a sum of 12 and the prefix subarray [8, 5] has a sum of 13. The difference is 12 - 13 = -1, which is within the threshold. Another contiguous subarray of length 4, [1, 4, 1, 9] with the prefix subarray [8, 5, 6], also yields an acceptable difference 1 + 4 + 1 + 9 - (8 + 5 + 6) = 15 - 19 = -4. Therefore, the answer is 4.


[6, 1, 4, 1]
 l
 r
left = 0

prefix_sum =0
curr_window = []
for right in range(n):
    if sum(curr_window) - prefix_sum <= threshold:
        max_len = max(max_len, right -left +1)
    else:
        curr_window.append(datasizes[right])
"""


def solution(dataSizes, threshold):
    max_len = 0  # maximum length of subarray
    n = len(dataSizes)  # length of dataSizes
    
    # (prefix_sum, index)
    #                    s, i
    prefix_sums = deque([0, -1])
    
    # [5, 15, 17, 11, 14, 11, 19], threshold = 4
    # end_index: 0
    #   current_prefix_sum = 5
    #   when doing diff, check all current deque items (all current prefix sums)
    #   diff = 5 - 2 * 0 -> no
    #   remove (0, -1) from the prefix_sums
    #   -> always: add (1, 5) to prefix_sums
    # end_index: 1
    #   current_prefix_sum = 20
    #   diff = 20 - 2 * 5 = 10 -> no
    #   remove (5, 0) from prefix_sums
    #   -> always: add (20, 1) to prefix_sums
    # end_index: 2
    #   current_prefix_sum = 37
    #   diff = 37 - 2 * 20 = -3 -> yes
    #   don't remove (20, 1)
    #   -> update max_len
    #   -> always: add (37, 2) to prefix_sums
    current_prefix_sum = 0
    for end_index in range(n):
        current_prefix_sum += dataSizes[end_index]
        while prefix_sums:
            if current_prefix_sum - 2 * prefix_sums[0][0] > threshold:
                prefix_sums.popleft()
            else:
                break
        max_len = max(max_len, end_index - prefix_sums[0][1])
        
        prefix_sums.append([current_prefix_sum, end_index])
    
    return max_len
