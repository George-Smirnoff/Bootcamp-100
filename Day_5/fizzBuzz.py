
def main():
    for i in range(1, 101):
        if i%3 == 0 or i%5 == 0:
            word = ''
            if i%3 == 0:
                word = 'fizz'
            if i%5 == 0:
                word += 'buzz'
            print(word)
        else:
            print(i)

if __name__ == '__main__':
    main()