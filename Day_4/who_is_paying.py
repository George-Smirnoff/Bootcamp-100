import random

def main():
    nameAsCSV = input("Give me everybody's names who can pay: ")
    name_map = nameAsCSV.split(",")

    print(f"{random.choice(name_map)} is going to buy a meal today")

if __name__ == "__main__":
    main()