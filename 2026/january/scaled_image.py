"""
Docstring for 2026.january.scaled_image
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-25
                        Scaled Image
Given a string representing the width and height of an image, and a number to scale the image, return the scaled width and height.

The input string is in the format "WxH". For example, "800x600".
The scale is a number to multiply the width and height by.
Return the scaled dimensions in the same "WxH" format.
"""
def scale_image(size, scale):
    w, h = size.split('x')
    new_w = int(w) * scale
    new_h = int(h) * scale
    return f"{int(new_w)}x{int(new_h)}"
print(scale_image("800x600", 2)   )    # should return "1600x1200".
print(scale_image("100x100", 10)  )    # should return "1000x1000".
print(scale_image("1024x768", 0.5))    # should return "512x384".
print(scale_image("300x200", 1.5) )    # should return "450x300".
