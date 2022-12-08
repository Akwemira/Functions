
"""

This function creates a text file holding the sum of groceries bought.

Args:
 Use list() to extract the values from the dictionary into a list
 Use sum() to get sum of the values
 Returns:
 Creates a .txt file with sum of groceries
"""


def grocery_cart(items):
    with open("receipt.txt", "w") as file:
        file.write(f"You bought {order}\n")
        file.write(f"Your price list is {price_list}\n")
        file.write(f"Your total cost is {Total_cost}\n")


order = {"tomato": 30, "thyme": 4.40, "garlic": 7.5, "rice": 10, "onion": 4, "fish": 9.99}
price_list = list(order.values())
Total_cost = sum(price_list)
grocery_cart(order)


