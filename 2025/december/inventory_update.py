"""
Docstring for december.inventory_update
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-12

                                        Inventory Update
Given a 2D array representing the inventory of your store, and another 2D array representing a shipment you have received, return your updated inventory.

Each element in the arrays will have the format: [quantity, "item"], where quantity is an integer and "item" is a string.
Update items in the inventory by adding the quantity of any matching items from the shipment.
If a received item does not exist in the current inventory, add it as a new entry to the end of the inventory.
Return inventory in the order it was given with new items at the end in the order they appear in the shipment.
For example, given an inventory of [[2, "apples"], [5, "bananas"]] and a shipment of [[1, "apples"], [3, "bananas"]], return [[3, "apples"], [8, "bananas"]].
"""
def update_inventory(inventory, shipment):
    inventory_map = {item: quantity for quantity, item in inventory}
    # this list will preserves the order of item
    inventory_item = [item for _, item in inventory]
    
    for quantity, item in shipment:
        if item in inventory_map:
            inventory_map[item] += quantity
        else:
            inventory_map[item] = quantity
            inventory_item.append(item)
    return [[inventory_map[item], item] for item in inventory_item]

print(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]])) # should return [[3, "apples"], [8, "bananas"]].
print(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]])) # should return [[3, "apples"], [8, "bananas"], [4, "oranges"]].
print(update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]])) # should return [[10, "apples"], [30, "bananas"], [20, "oranges"]].
print(update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]])) # should return [[1, "Bowling Ball"], [0, "Dirty Socks"], [1, "Hair Pin"], [0, "Microphone"], [1, "Half-Eaten Apple"], [1, "Toothpaste"]].