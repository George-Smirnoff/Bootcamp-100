import random

test_seed = input("Create a seed number: ")
random.seed(test_seed)

if random.randint(0, 1) == 1:
    print("Heads")
else:
    print("Tails")