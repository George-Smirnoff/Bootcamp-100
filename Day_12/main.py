import random

level = {
    'easy': 10,
    'hard': 5
}

def generateNumber():
    print("I'm thinking of a number between 1 and 100.")
    return random.randint(1, 100)

def main():
    print("Welcome to the Number Guessing Game!")
    number = generateNumber()
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    for i in range(level[difficulty], 0, -1):
        print(f"You have {i} attempts ramaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        elif guess == number:
            print("You got it!")
            exit()
    print("You lose...")


if __name__ == '__main__':
    main()