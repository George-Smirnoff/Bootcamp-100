import ASCII


def sum(a, b):
    return a + b

def deduct(a, b):
    return a - b

def multiply(a, b):
    return a * b

def devide(a, b):
    return a / b

def main():
    print(ASCII.calculator)
    number1 = int(input("What is your first number? "))

    iteration = True
    while iteration:
        operation = input("Pick an operation:\n-\n+\n*\n/\n")
        number2 = int(input("What is next number? "))
        # Choose operation
        #2 Another way is to crate a map with symbol/function name match
        match operation:
            case "+":
                result = sum(number1, number2)
            case "-":
                result = deduct(number1, number2)
            case "*":
                result = multiply(number1, number2)
            case "/":
                result = devide(number1, number2)
            case _:
                print("Unknown operation...")
                exit(0)
        print(f"{number1} {operation} {number2} = {result}")
        next_iteration = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ")
        if "y" in next_iteration:
            number1 = result
        else:
            #2 Use recursion for calculation
            iteration = False
            main()
            #1 number1 = int(input("What is your first number? "))


if __name__ == '__main__':
    main()