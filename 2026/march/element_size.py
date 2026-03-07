"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-07
Element Size
Given a window size, the width of an element in viewport width "vw" units, and the height of an element in viewport height "vh" units, determine the size of the element in pixels.

The given window size and returned element size are strings in the format "width x height", "1200 x 800" for example.
"vw" units are the percent of window width. "50vw" for example, is 50% of the width of the window.
"vh" units are the percent of window height. "50vh" for example, is 50% of the height of the window.
"""
def get_element_size(window_size, element_vw, element_vh):
    width_str, height_str = window_size.split('x')

    window_width, window_height = int(width_str), int(height_str)

    vw = int(element_vw[:-2])
    vh = int(element_vh[:-2])

    element_width = round((window_width * vw) / 100)
    element_height = round((window_height * vh) / 100)

    return f"{element_width} x {element_height}"

print(get_element_size("1200 x 800", "50vw", "50vh"))      # should return "600 x 400".
print(get_element_size("320 x 480", "25vw", "50vh"))       # should return "80 x 240".
print(get_element_size("1000 x 500", "7vw", "3vh"))        # should return "70 x 15".
print(get_element_size("1920 x 1080", "95vw", "100vh"))    # should return "1824 x 1080".
print(get_element_size("1200 x 800", "0vw", "0vh"))        # should return "0 x 0".
print(get_element_size("1440 x 900", "100vw", "114vh"))    # should return "1440 x 1026".