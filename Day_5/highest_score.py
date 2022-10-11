
def main():
    scores = input("Input a scores of everyone in class with a space: ")
    scores_list = scores.split(' ')

    max_score = 0
    for score in scores_list:
        score = int(score)
        if score > max_score:
            max_score = score

    print(f"Max score in class is {max_score}.")

if __name__ == '__main__':
    main()