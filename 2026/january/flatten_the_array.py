"""
Docstring for 2026.january.flatten_the_array
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-28
Flatten the Array
Given an array that contains nested arrays, return a new array with all values flattened into a single, one-dimensional array. Retain the original order of the items in the arrays.
"""
def flatten(arr):

    # recursion
    # output = []
    
    # def flat(item):
    #     for x in item:
    #         if isinstance(x, list):
    #             flat(x)
    #         else:
    #             output.append(x)
    # flat(arr)
    # return output

    # iteration
    output = []
    stack = arr[::-1]

    while stack:
        curr = stack.pop()
        if isinstance(curr, list):
            stack.extend(curr[::-1])
            print(stack)
        else:
            output.append(curr)
    return output[::1]

print(flatten([1, [2, 3], 4])) # should return [1, 2, 3, 4].
print(flatten([5, [4, [3, 2]], 1])) # should return [5, 4, 3, 2, 1].
print(flatten(["A", [[[["B"]]]], "C"])) # should return ["A", "B", "C"].
print(flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]])) # should return ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"].
print(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]])) # should return ["red","blue","green","yellow","purple","orange","pink","brown"]