'''
calculator.py

'''



'''
This function adds two numbers
Arguments: num1, num2
Return: num1 + num2
'''
def add(a, b):
    return a + b
'''
This function calculates the remainder of two numbers
Arguments: num1, num2
Return: num1 - num2
'''
def subtract(a, b):
    return a - b 
'''
This function calculates the product of two numbers
Arguments: num1, num2
Return: num1 * num2
'''
def multiply(a, b):
    return a * b
'''
This function calculates the quotient of two numbers
Arguments: num1, num2
Return: num1 / num2
'''
def divide(a, b):
    return a / b
'''
This function calculates the exponential of one number raised to another
Arguments: num1, num2
Return: num1 ** num2
'''
def exponential(a, b):
    return a ** b


operators = ["+", "-", "*", "/", "**"]  

if __name__ == '__main__':

    while True:
        user_choice = input("Which operation do you want to perform?\nIf none please, enter q to exit calculator\n")
        if user_choice in operators:
            num1 = float(input("Enter first number: \n"))
            num2 = float(input("Enter second number: \n"))
            
            if user_choice == '+':
                sum = add(num1, num2)
                print(f'The sum of {num1} and {num2} is: {sum}\n')

            elif user_choice == '-':
                remainder = subtract(num1,num2)
                print(f'The remainder of {num1} minus {num2} is: {remainder}\n')

            elif user_choice == '*':
                product = multiply(num1, num2)
                print(f'The product of {num1} and {num2} is: {product}\n')

            elif user_choice == '**':
                value = exponential(num1, num2)
                print(f'The value of {num1} power of {num2} is: {value}\n')

            elif user_choice == '/':
                try: # handling exception when divisor is 0
                    quotient = divide(num1, num2)
                    print(f'The quotient of {num1} and {num2} is: {quotient}\n')
                except:
                    print(f'This calculator cannot handle division of {num1} by 0 as divisor.\nPlease try another number as divisor\n')
            else:
                print('Wrong operator. Available operators are: +, -, /, *, **\n')

        elif user_choice == "q":
            print("Exiting calculator. Thank you\n")
            break
        
        else:
            print('Wrong operator. Available operators are: +, -, /, *, **\n')
    


