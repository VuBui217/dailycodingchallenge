"""
Docstring for 2026.january.free_shipping
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-18
                        Free Shipping
Given an array of strings representing items in your shopping cart, and a number for the minimum order amount to qualify for free shipping, determine if the items in your shopping cart qualify for free shipping.

The given array will contain items from the list below:

Item	Price
"shirt"	34.25
"jeans"	48.50
"shoes"	75.00
"hat"	19.95
"socks"	15.00
"jacket"109.95
"""
def gets_free_shipping(cart, minimum):
    items_map = {"shirt": 34.25, "jeans": 48.50, "shoes": 75.00, "hat": 19.95, "socks": 15.00, "jacket": 109.95}

    total = sum([items_map[item] for item in cart])
    return total >= minimum

print(gets_free_shipping(["shoes"], 50)                                        )   #  should return True.
print(gets_free_shipping(["hat", "socks"], 50)                                 )   #  should return False.
print(gets_free_shipping(["jeans", "shirt", "jacket"], 75)                     )   #  should return True.
print(gets_free_shipping(["socks", "socks", "hat"], 75)                        )   #  should return False.
print(gets_free_shipping(["shirt", "shirt", "jeans", "socks"], 100)            )   #  should return True.
print(gets_free_shipping(["hat", "socks", "hat", "jeans", "shoes", "hat"], 200))   #  should return False.