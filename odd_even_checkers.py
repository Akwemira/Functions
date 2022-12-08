""" 
This function checks for odd or even numbers.

Args:
 use modulo operand (%). user input % 2.
 Returns:
 If the result is 0, user input is an even number. Else, an odd number.
"""

def CheckEvenOdd(num): 
  if (num % 2 == 0): 
    print(num," is EVEN")
  else: 
    print(num," is ODD")

user_input = int(input("Choose a number from 0 to 100\n"))
CheckEvenOdd(user_input)

