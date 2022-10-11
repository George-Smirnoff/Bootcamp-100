def main():
    hights = input("Input a hight of everyone in class with a space: ")
    hights_list = hights.split(' ')

    sum = 0
    for hight in hights_list:
        sum += int(hight)

    average = int(sum/len(hights_list))

    print(f"Everage hight in class is {average}.")

if __name__ == '__main__':
    main()