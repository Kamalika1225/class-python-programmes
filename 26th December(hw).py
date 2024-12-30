class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b

def get_number(prompt):
    return float(input(prompt))

calculator = Calculator()

num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
operation = input("Enter an operation (+, -, *, /): ")

if operation == '+':
    result = calculator.add(num1, num2)
elif operation == '-':
    result = calculator.subtract(num1, num2)
elif operation == '*':
    result = calculator.multiply(num1, num2)
elif operation == '/':
    try:
        result = calculator.divide(num1, num2)
    except ZeroDivisionError:
        result = "Error: Division by zero."

print(f"The result is: {result}")
