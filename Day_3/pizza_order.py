
def total_price(size, add_pepperoni, extra_cheese):
    sum = 0
    positiveInput = ('Y', 'y')
    negativeInput = ('N', 'n')

    # Choose pizza price
    match size:
        case "S":
            sum += 15
        case "M":
            sum += 20
        case "L":
            sum += 25
        case _:
            print("Unexpected pizza size...")
            exit(0)

    # Add pepperoni price
    if add_pepperoni.endswith(positiveInput):
        match size:
            case "S":
                sum += 2
            case "M":
                sum += 3
            case "L":
                sum += 3
        print("Added the pepperoni!")
    elif add_pepperoni.endswith(negativeInput):
        print("Pizza will be without pepperoni!")
    else:
        print("Didn't get the point about pepperoni...")

    # Add cheese price
    if extra_cheese.endswith(positiveInput):
        sum += 1
        print("Added the cheese!")
    elif extra_cheese.endswith(negativeInput):
        print("Pizza will be without cheese!")
    else:
        print("Didn't get the point about cheese...")

    return sum

def main():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size of pizza do you want? S, M, or L? ")
    add_pepperoni = input("Do you want to add a pepperoni? ")
    extra_cheese = input("Do you want extra cheese? ")

    sum = total_price(size, add_pepperoni, extra_cheese)
    print(f"You final bill is: {sum}.")

if __name__ == "__main__":
    main()