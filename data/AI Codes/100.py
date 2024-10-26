import operator

def calculate(expression):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    for op in operators:
        if op in expression:
            left, right = map(float, expression.split(op))
            return operators[op](left, right)
    return "Invalid operator."

def main():
    print("Command-Line Calculator")
    expression = input("Enter calculation (e.g., 5 + 3): ")
    result = calculate(expression)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
