"""
multiply_odd_even_numbers.py
"""
from math import prod

numbers = [8,9,11,20,32,101,100]

def generate_even_numbers():
    '''
    This function generates list of even numbers
    Argument: None
    Returns: list of all (x % 2 ==0) from numbers
    '''
    return [x for x in numbers if x % 2==0]

def prod_even_numbers(even_number_list):
    '''
    This function calculates product of a list 
    Parameter: even_number_list
    Argument: even_number_list
    Returns: prod(even_number_list)
    '''
    return prod(even_number_list)

if __name__ == '__main__':
    
    even_number_list = generate_even_numbers()

    print(f'\nList of even numbers{even_number_list}\n')

    product = prod_even_numbers(even_number_list)

    print(f"The product of even numbers is {product}\n")

