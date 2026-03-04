"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-04
                    Playing Card Values
Given an array of playing cards, return a new array with the numeric value of each card.

Card Values:

An Ace ("A") has a value of 1.
Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.
Suits:

Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").
Card Format:

Each card is represented as a string: "valueSuit". For Example: "AS" is the Ace of Spades, "10H" is the Ten of Hearts, and "QC" is the Queen of Clubs.
"""
def card_values(cards):
    card_maps = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    
    return [card_maps[card[:-1]] for card in cards]

print(card_values(["3H", "4D", "5S"]))                 # should return [3, 4, 5].
print(card_values(["AS", "10S", "10H", "6D", "7D"]))   # should return [1, 10, 10, 6, 7].
print(card_values(["8D", "QS", "2H", "JC", "9C"]))     # should return [8, 10, 2, 10, 9].
print(card_values(["AS", "KS"]))                       # should return [1, 10].
print(card_values(["10H", "JH", "QH", "KH", "AH"]))    # should return [10, 10, 10, 10, 1].