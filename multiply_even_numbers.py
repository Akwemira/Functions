"""
multiply_odd_even_numbers.py
"""
from math import prod

numbers = [8,9,11,20,32,101,100]
'''
This function generates list of even numbers
Argument: list called numbers
Returns: list of all (x % 2 ==0) from numbers
'''
def generate_even_numbers():
    return [x for x in numbers if x % 2==0]
'''
This function calculates product of a list 
Argument: list of even numbers
Returns: product
'''
def prod_even_numbers(even_number_list):
    return prod(even_number_list)

if __name__ == '__main__':
    
    even_number_list = generate_even_numbers()

    print(f'\nList of even numbers{even_number_list}\n')

    product = prod_even_numbers(even_number_list)

    print(f"The product of even numbers is {product}\n")

