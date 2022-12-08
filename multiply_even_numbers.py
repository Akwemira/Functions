"""

This function computes the product of a list of even numbers.

Args:
 Use x for x list comprehension to create a new list
 Use x % 2 ==0 to fish out even numbers
 Use from math module import prod function to get product of all elements in iterable
 Returns:
 Product of even numbers
"""
from math import prod

def even_numbers(x):
   
    product = prod(even_number_list)
    print(f"\nlist of even numbers is {even_number_list}\n")
    print(f"Their product is {product}\n")

numbers = [8,9,11,20,32,101,100]
even_number_list = [x for x in numbers if x % 2==0]
even_numbers(even_number_list)