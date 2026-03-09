"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-08
                    HSL Validator
Given a string, determine whether it is a valid CSS hsl() color value.

A valid HSL value must be in the format "hsl(h, s%, l%)", where:

h (hue) must be a number between 0 and 360 (inclusive).
s (saturation) must be a percentage between 0% and 100%.
l (lightness) must be a percentage between 0% and 100%.
Spaces are only allowed:

After the opening parenthesis
Before and/or after the commas
Before and/or after closing parenthesis
Optionally, the value can end with a semi-colon (";").
For example, "hsl(240, 50%, 50%)" is a valid HSL value.
"""
def is_valid_hsl(hsl):
    open_parenthese = hsl.index('(')
    close_parenthese = hsl.index(')')

    hsl_part1 = hsl[:open_parenthese]
    
    if ' ' in hsl_part1:
        return False
    
    hsl_part2 = hsl[open_parenthese + 1: close_parenthese]

    hsl_values = hsl_part2.split(',')

    if len(hsl_values) != 3:
        return False
    h_str, s_str, l_str = hsl_values

    if s_str.strip()[-1] != '%' or l_str.strip()[-1] != '%':
        return False

    try:
        h, s, l = int(h_str.strip()), int(s_str.strip()[:-1]), int(l_str.strip()[:-1])
    except ValueError:
        return False
    
    if h < 0 or h > 360:
        return False
    if s < 0 or s > 100:
        return False
    if l < 0 or l > 100:
        return False
    return True

    # Solution 2
    # Using regex
    # import re
    # pattern = r'^hsl\(\s*(\d+)\s*,\s*(\d+)%\s*,\s*(\d+)%\s*\)\s*;?$'
    # match = re.fullmatch(pattern, hsl)
    # if not match:
    #     return False
    # h, s, l = int(match.group(1)), int(match.group(2)), int(match.group(3))
    # return 0 <= h <= 360 and 0 <= s <= 100 and 0 <= l <= 100


print(is_valid_hsl("hsl(240, 50%, 50%)"))                  # should return True.
print(is_valid_hsl("hsl( 200 , 50% , 75% )"))              # should return True.
print(is_valid_hsl("hsl(99,60%,80%);"))                    # should return True.
print(is_valid_hsl("hsl(0, 0%, 0%) ;"))                    # should return True.
print(is_valid_hsl("hsl(  10  ,  20%   ,  30%   )    ;"))  # should return True.
print(is_valid_hsl("hsl(361, 50%, 80%)"))                  # should return False.
print(is_valid_hsl("hsl(300, 101%, 70%)"))                 # should return False.
print(is_valid_hsl("hsl(200, 55%, 75)"))                   # should return False.
print(is_valid_hsl("hsl (80, 20%, 10%)"))                  # should return False.