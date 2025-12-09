def run_calculator(a, b, c):
        if c == '+':
            return a + b
        elif c == '-':
            return a - b
        elif c == '*':
            return a * b
        elif c == '/':
            if b != 0:
                return a / b
            else:
                return "Error: Division by zero"
        else:
            return "Error: Invalid operator"
        
def main():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    z = input("Enter operator (+, -, *, /): ")
    return run_calculator(x, y, z)

if __name__ == "__main__":
    try:
        result = main()
        print(f"Result: {result}")
        exit(0)
    except Exception:
        print("Error")
        exit(1)
