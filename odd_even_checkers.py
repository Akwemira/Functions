'''
odd_even_checkers.py
'''

def CheckEvenOdd(num):
  '''
  This function checks for odd or even numbers.
  Args: (num % 2) == 0.
  Returns: none
  ''' 
  if (num % 2 == 0): 
    print(num," is EVEN")
  else: 
    print(num," is ODD")

if __name__ == '__main__':

  user_input = int(input("Choose a number from 0 to 100\n"))
  CheckEvenOdd(user_input)

