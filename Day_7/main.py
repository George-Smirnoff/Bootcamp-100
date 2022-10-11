import random
import ASCII

# Create a set with Uniq letters of the game word
def uniqLetterSet(word):
    return set(word)

def main():
    word_list = ["aardvark", "baboon", "camel"]
    lives_num = len(ASCII.lives)

    # Print Logo
    print(ASCII.hangman)

    # choose the word for game
    game_word = random.choice(word_list).lower()
    word_lenght = len(game_word)
    status_bar = list('_' * word_lenght)

    letterSet = uniqLetterSet(game_word)

    while lives_num > 0:
        print(''.join(status_bar))
        letter = input("Guest a letter: ").lower()

        # Check the letter in game word
        if letter in letterSet:
            letterSet.remove(letter)

            # Update status bar with opened letter
            for position in range(word_lenght):
                replace = game_word[position]
                if replace == letter:
                    status_bar[position] = letter
            # ^ imroved above ^
            # Conclusion: You can iterate with string's letters or their position in string
            # j = 0
            # for i in game_word:
            #     if i == letter:
            #         status_bar[j] = letter
            #     j += 1

            # Check if all letters found
            if len(letterSet) == 0:
                print(''.join(status_bar))
                print("You win the game!")
                exit(0)
        else:
            print(f"You guessed {letter}, that's not in the word. You lose a life.")
            lives_num -= 1
            print(ASCII.lives[lives_num])

    print("You lose the game...")

if __name__ == '__main__':
    main()