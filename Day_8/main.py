from string import ascii_lowercase
#1 import operator

def chipher(message, shift, operation):
    # generate lowercase alphabet
    alphabet = list(ascii_lowercase)
    result = []

    # Encrypt or decrypt
    #1 ops = {"e": operator.add, "d": operator.sub}
    if operation == "d":
        shift *= -1

    for i in range(len(message)):
        char = message[i]
        if char in alphabet:
            position = ascii_lowercase.index(char)
            #1 replacement_position = ops[operation](position, shift)%len(alphabet)
            # Conclusion: To choose the '+' or '-' operation you can just reassign the value
            # with positive or negative sign
            replacement_position = (position + shift) % len(alphabet)
            result.append(alphabet[replacement_position])
        else:
            result.append(char)

    print(''.join(result))


def main():
    statement = True
    while statement:
        operation = input("Type 'e' tp encrypt, type 'd' to decrypt: ").lower()
        if operation in "de":
            message = input("Type your message:\n")
            shift = int(input("Type the shift number:\n"))
            chipher(message, shift, operation)
        else:
            print("Unknown operation. Try again...")

        iteration = input("Type 'no/n' to stop.\n").lower()
        if "n" in iteration:
            statement = False
            print("Good Bye!")

if __name__ == '__main__':
    main()