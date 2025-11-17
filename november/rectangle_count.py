"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-16

                                            Rectangle Count
Given two positive integers representing the width and height of a rectangle, determine how many rectangles can fit in the given one.

Only count rectangles with integer width and height.
For example, given 1 and 3, return 6. Three 1x1 rectangles, two 1x2 rectangles, and one 1x3 rectangle.
"""
def count_rectangles(width, height):
    # Using combinations
    # See the rectangle as a frid created by formed multiple vertical lines and horizontal line
    # We will have width+1 horizontal lines
    # and height+1 vertical lines
    # We need to pick 2 horizontal line from (width+1) and 2 veritcal lines from (height+1) to form a rectangle

    num_of_options_for_horizontal_line = ((width + 1) * width) / 2
    num_of_options_for_vertival_line = ((height + 1) * height) / 2

    total = (int)(num_of_options_for_horizontal_line * num_of_options_for_vertival_line)
    return total

print(count_rectangles(1, 3)  )    # should return 6.
print(count_rectangles(3, 2)  )    # should return 18.
print(count_rectangles(1, 2)  )    # should return 3.
print(count_rectangles(5, 4)  )    # should return 150.
print(count_rectangles(11, 19))    # should return 12540.