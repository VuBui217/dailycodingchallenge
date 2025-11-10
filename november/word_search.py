"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-09

                                    Word Search
Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.

The given matrix will be filled with all lowercase letters (a-z).
The word to find will always be in the matrix exactly once.
The word to find will always be in a straight line in one of these directions:
left to right
right to left
top to bottom
bottom to top
For example, given the matrix:

[
  ["a", "c", "t"],
  ["t", "a", "t"],
  ["c", "t", "c"]
]
And the word "cat", return:

[[0, 1], [2, 1]]
Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the indices for the "t" (end of the word).
"""
def find_word(matrix, word):
    # Matrix contains only lowercase letters
    # Only one solution in the matrix
    # Word always in straight line:
    #   left to right
    #   right to left
    #   top to bottom
    #   bottom to top

    # Traverse the matrix
    # If the current cell equals to the first letter of word
    # We'll explore all the direction from that cell, and a variable to keep track the word len, when move to either direction

    rows = len(matrix)
    cols = len(matrix[0])
    word_len = len(word)

    # Directions:
    directions = [
        [0, 1], #left to right
        [0, -1], #right to left
        [1, 0], #top to bottom
        [-1, 0]  #bottom to top
    ]
    # for i in range(rows):
    #     for j in range(cols):
    #         if matrix[i][j] == word[0]:
    #             # Explore all the directions from the current cell
    #             for dr, dc in directions:
    #                 r, c = i, j
    #                 k = 0
    #                 while (0 <= r < rows) and (0 <= c < cols) and k < word_len and (matrix[r][c] == word[k]):
    #                     r += dr
    #                     c += dc
    #                     k +=1
    #                 if k == word_len:
    #                     end_r = i + dr * (word_len - 1)
    #                     end_c = j + dc * (word_len - 1)
    #                     return [[i, j], [end_r, end_c]]

    """
    Using recursion
    """

    def dfs(i, j, dr, dc, k):
        if k == len(word):
            return True
        if not (0 <= i < len(matrix) and 0 <= j < len(matrix[0])):
            return False
        if [i][j] != word[k]:
            return False
        return dfs(i + dr, j + dc, dr, dc, k + 1)
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == word[0]:
                for dr, dc in directions:
                    if dfs(i, j, dr, dc, 0):
                        end_r = i + dr * (word_len - 1)
                        end_c = j + dc * (word_len - 1)
                        return [[i, j], [end_r, end_c]]
                    

                    
print(find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat")) # [[0, 1], [2, 1]]

print(find_word([["f", "x", "o", "x"], 
           ["o", "x", "o", "f"], 
           ["f", "o", "f", "x"], 
           ["f", "x", "x", "o"]], "fox")) # [[1, 3], [1, 1]]