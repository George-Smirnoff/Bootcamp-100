
def main():
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]

    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}\n")
    position = input("Where do you want to left the treasure? ")
    colomn = int(position[0]) - 1
    row = int(position[1]) -1

    map[row][colomn] = "X"

    print(f"{row1}\n{row2}\n{row3}\n")

if __name__ == "__main__":
    main()