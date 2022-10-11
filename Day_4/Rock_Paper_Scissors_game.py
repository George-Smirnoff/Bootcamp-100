import random
import ASCII

def main():
    user_hand = int(input("What do you choose? type 0 for Rock, 1 for Paper, 2 for Scissors: "))

    # Validation
    if user_hand >= 3 or user_hand < 0:
        print(" You typed an invalid number, you lose!")
        exit(0)

    # random choice for PC
    pc_hand = random.randint(0, 2)

    # print hands
    hands = [ASCII.rock, ASCII.paper, ASCII.scissors]
    print(f"User choice:\n{hands[user_hand]}\n")
    print(f"Computer choice:\n{hands[pc_hand]}\n")

    # win logic
    if user_hand == 0 and pc_hand == 2:
        print("You win!")
    elif user_hand == 2 and pc_hand == 0:
        print("You lose!")
    elif pc_hand > user_hand:
        print("Computer win!")
    elif user_hand > pc_hand:
        print("You win!")
    elif pc_hand == user_hand:
        print("It's a draw.")

if __name__ == '__main__':
    main()