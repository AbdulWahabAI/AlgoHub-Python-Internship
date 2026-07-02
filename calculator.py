# Main math functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Can't divide by zero!"
    return a / b

def run_calculator():
    print("\n--- My Custom Calculator ---")
    
    try:
        x = float(input("First number: "))
        y = float(input("Second number: "))
    except ValueError:
        print("Please enter valid numbers next time.")
        return

    print("Options: +, -, *, /")
    op = input("Pick an operation: ").strip()

    if op == '+':
        print(f"Result: {x} + {y} = {add(x, y)}")
    elif op == '-':
        print(f"Result: {x} - {y} = {subtract(x, y)}")
    elif op == '*':
        print(f"Result: {x} * {y} = {multiply(x, y)}")
    elif op == '/':
        print(f"Result: {divide(x, y)}")
    else:
        print("Invalid operator selected.")