
def splitBill(total, peopleNumber, tips):
    return round((total + (total*tips/100))/peopleNumber, 1)

def main():

    total = float((input('What a total bill do we have? ')))
    peopleNumber = int((input('How many people to split the the bill? ')))
    tips = int((input('What a persentage tip would you like to give? 5, 10, or 15? ')))
    print(splitBill(total, peopleNumber, tips))

if __name__ == "__main__":
    main()