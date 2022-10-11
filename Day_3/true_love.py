
def calcSymbols(symbol, word):
    return word.lower().count(symbol)


def loveCalc(name1, name2):
    first_match = "true"
    second_match = "love"
    first_sum = 0
    second_sum = 0

    for i in first_match:
        first_sum += calcSymbols(i, name1)
        first_sum += calcSymbols(i, name2)
    for i in second_match:
        second_sum += calcSymbols(i, name1)
        second_sum += calcSymbols(i, name2)
    return str(first_sum) + str(second_sum)

def main():
    print("Welcome to love calculator!")
    name1 = input("What is your name?\n")
    name2 = input("What is their name?\n")
    match = loveCalc(name1, name2)
    print(f"You have match on {match}%.")

if __name__ == "__main__":
    main()