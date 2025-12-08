"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-08
                                Pounds to Kilograms
Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

Replace "(lbs)" with the input number.
Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
1 pound equals 0.453592 kilograms.
If the input is 1, use "pound" instead of "pounds".
If the converted value is 1, use "kilogram" instead of "kilograms".     
"""
def convert_to_kgs(lbs):
    lbs_to_kgs = 0.453592 * lbs
    kgs_rounded = round(lbs_to_kgs, 2)
    
    kgs_strs = f"{lbs_to_kgs:.2f}"
    
    p_word = "pound" if lbs == 1 else "pounds"
    k_word ="kilogram" if kgs_rounded == 1 else "kilograms"
    return f"{lbs} {p_word} equals {kgs_strs} {k_word}."

print(convert_to_kgs(1)      ) # should return "1 pound equals 0.45 kilograms.".
print(convert_to_kgs(0)      ) # should return "0 pounds equals 0.00 kilograms.".
print(convert_to_kgs(100)    ) # should return "100 pounds equals 45.36 kilograms.".
print(convert_to_kgs(2.5)    ) # should return "2.5 pounds equals 1.13 kilograms.".
print(convert_to_kgs(2.20462)) # should return "2.20462 pounds equals 1.00 kilogram."