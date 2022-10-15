import pandas as pd

def main():
    alphabet_data = pd.read_csv('phonetic_alphabet.csv', header=None)
    alphabet_dict = {row[0]: row[1] for (_, row) in alphabet_data.iterrows()}

    # Interactive part
    # Improve: Use Upper one time for input:
    # word = input("Type you word to find phonetic alters: ").upper()
    word = input("Type you word to find phonetic alters: ")
    result = [alphabet_dict[letter.upper()] for letter in word]
    print(result)

if __name__ == '__main__':
    main()