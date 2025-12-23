"""
Docstring for december.traveling_shopper
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-22
                        Traveling Shopper
Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.

The given amount will be in the format ["Amount", "Currency Code"]. For example: ["150.00", "USD"] or ["6000", "JPY"].
Each array item you want to purchase will be in the same format.
Use the following exchange rates to convert values:

Currency	1 Unit Equals
USD	        1.00 USD
EUR	        1.10 USD
GBP	        1.25 USD
JPY	        0.0070 USD
CAD	        0.75 USD
If you can afford all the items in the list, return "Buy them all!".
Otherwise, return "Buy the first X items.", where X is the number of items you can afford when purchased in the order given.
"""
def preprocessing(items, table):
    prices_in_usd = []
    for price_str, unit in items:
        price = float(price_str)
        prices_in_usd.append(price * table[unit])
    return prices_in_usd
def buy_items(funds, items):
    table = {"USD": 1.00, "EUR": 1.10, "GBP": 1.25, "JPY": 0.0070, "CAD": 0.75}
    total, unit = float(funds[0]), funds[1]
    total_in_usd = total * table[unit]
    processed_items = preprocessing(items, table)

    items_count = 0

    for price in processed_items:
        total_in_usd -= price
        if total_in_usd < 0:
            break
        items_count += 1
    
    return f"Buy them all!" if items_count == len(items) else f"Buy the first {items_count} items."

print(buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]])                                                     )   # should return "Buy the first 2 items.".
print(buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]])                                                                       )   # should return "Buy them all!".
print(buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]) )   # should return "Buy the first 3 items.".
print(buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]])       )   # should return "Buy them all!".
print(buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]]))   # should return "Buy the first 5 items.".