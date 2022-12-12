
"""
sales.py
"""

order = {"tomato": 30, "thyme": 4.40, "garlic": 7.5, "rice": 10, "onion": 4, "fish": 9.99}
'''
    Description: this function sums values from a dictionary called order
    Argument: order.values()
    Returns: sum(float)
'''  
def calculate_sum():
    return sum(order.values())
   
'''
    Description: this function creates a file and writes total of an order to it 
    Argument: total_value
    Returns: None
'''    
def generate_receipt():
    with open("receipt.txt", "w") as file:
        file.write(f"===WELCOME TO ONE-STOP-SHOP===\n")
        file.write(f"  *******Your Receipt*******\n\n")
        file.write(f"  Your total is ${total_value}\n")

if __name__ == '__main__':

    try:
        total_value = calculate_sum()
        print(f'Your total is: ${total_value}')

    except:
        print("We are expecting a valid dictionary as data type")

    generate_receipt()



