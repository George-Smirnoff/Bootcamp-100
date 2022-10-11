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

    list_pwd = []

    list_pwd += random.choices(letters, k = nr_letters)
    list_pwd += random.choices(numbers, k = nr_numbers)
    list_pwd += random.choices(symbols, k = nr_symbols)
    random.shuffle(list_pwd)
    print(''.join(map(str, list_pwd)))

if __name__ == '__main__':
    main()