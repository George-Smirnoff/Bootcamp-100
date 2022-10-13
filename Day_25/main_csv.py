import csv

def main():
    temperature = []
    filepath = 'forecast.csv'
    # with open(filepath, 'r') as file:
    #     list = file.readlines()

    with open(filepath, 'r') as file:
        data = csv.reader(file)
        for row in data:
            try:
                temperature.append(int(row[1]))
            except ValueError:
                pass

    print(temperature)
if __name__ == '__main__':
    main()