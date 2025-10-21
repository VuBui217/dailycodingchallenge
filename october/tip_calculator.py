"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-20

Tip Calculator
Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.

Prices will be given in the format: "$N.NN".
Custom tip percents will be given in this format: "25%".
Return amounts in the same "$N.NN" format, rounded to two decimal places.
For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].
"""

def calculate_tips(meal_price, custom_tip):
    # Convert input to number
    price = float(meal_price.replace('$', ''))
    custom = float(custom_tip.replace('%',''))

    # Calculate the tips for 15%, 20%, and custom_tip
    tip_15 = price*0.15
    tip_20 = price*0.20
    tip_custom = price*(custom/100)

    return [f'${tip_15:.2f}',f'${tip_20:.2f}',f'${tip_custom:.2f}']

print(calculate_tips("$10.00", "25%"))