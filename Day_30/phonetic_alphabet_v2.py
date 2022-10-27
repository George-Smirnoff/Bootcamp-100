import pandas as pd

def main():
    alphabet_data = pd.read_csv('phonetic_alphabet.csv', header=None)
    alphabet_dict = {row[0]: row[1] for (_, row) in alphabet_data.iterrows()}

    # Interactive part
    word = input("Type you word to find phonetic alters: ").upper()
    try:
        result = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Only letters in alphabet please")
        main()
    else:
        print(result)

if __name__ == '__main__':
    main()