"""
link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-22
                                    Recipe Scaler
Given an array of recipe ingredients and a number to scale the recipe, return an array with the quantities scaled accordingly.

Each item in the given array will be a string in the format: "quantity unit ingredient". For example "2 C Flour".
Scale the quantity by the given number. Do not include any trailing zeros and do not convert any units.
Return the scaled items in the same order they are given.       
"""
def scale_recipe(ingredients, scale):
    output = []
    for item in ingredients:
        quantity, unit, ingredient = item.split(" ", 2) # Using max split
        new_quantity = scale * float(quantity)
        formatted_new_quantity = "{:g}".format(new_quantity)
        output.append(f"{formatted_new_quantity} {unit} {ingredient}")
    return output

print(scale_recipe(["2 C Flour", "1.5 T Sugar"], 2)) # should return ["4 C Flour", "3 T Sugar"]

print(scale_recipe(["2 C All-purpose Flour", "1 t Baking Soda", "1 t Salt", "1 C Butter", "0.5 C Sugar", "0.5 C Brown Sugar", "1 t Vanilla Extract", "2 C Chocolate Chips"], 2.5))