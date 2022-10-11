import random

def main():
    random_integer = random.randint(0, 10)
    print(random_integer)

    random_float = random.uniform(-9.9, 9.9)
    print(round(random_float, 2))

if __name__ == "__main__":
    main()