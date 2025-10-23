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
