""" 
This function carries out some arithmetic operations on 2 user input numbers.

Args:
 x by y using any operand of choice.
 Returns:
 The result of the operation on x and y.
"""

def f(x,y):
    if operation in operands:
        result = eval(f"{x} {operation} {y}")
        return result
        
    else:
        print(f"invalid operation")



operands = ["+", "-", "*", "/", "**"]
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Do you want to +, -, /, *, **, today? Choose one: \n")
f(num1,num2)
print(f"your answer is {f(num1,num2)}")
print(f"Thank you for using our calculator")
