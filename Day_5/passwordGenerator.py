import random
import string


def main():
    letters = list(string.ascii_letters)
    numbers = list(range(0, 10))
    symbols = list(r'\/:*?"<>|()#$%@^&')


    print("Welcome to the Password Generator!")
    nr_letters = int(input("How many letters would you like in your password? "))
    nr_numbers = int(input("How many numbers would you like? "))
    nr_symbols = int(input("How many special symbols would you like? "))

    lenght = nr_letters + nr_numbers + nr_symbols
    password = ''
    for i in range(0, lenght+1):
        choice = random.randint(0, 2)
        if choice == 0:
            password += random.choice(letters)
        if choice == 1:
            password += str(random.choice(numbers))
        if choice == 2:
            password += random.choice(symbols)
    print(password)

if __name__ == '__main__':
    main()