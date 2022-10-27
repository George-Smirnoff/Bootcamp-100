def make_pie(index):
    fruits = ["Apple", "Pear", "Orange"]
    try:
        fruit = fruits[index]
        print(fruit + 'pie')
    except IndexError:
        print('Fruit pie')
    else:
        print(fruit + ' pie')

def main():
    make_pie(2)

if __name__ == '__main__':
    main()