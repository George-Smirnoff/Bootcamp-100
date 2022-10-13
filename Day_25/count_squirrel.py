import pandas

def main():
    filename = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
    #1 gray_num = 0
    #1 cinnamon_num = 0
    #1 black_num = 0

    data = pandas.read_csv(filename)
    # Another way to read the column
    #4 Read as MultiIndex
    #4 data = pandas.read_csv(filename) ,
    #4                        usecols=["Primary Fur Color"])

    # Embedded functionality
    fur_color_data = data["Primary Fur Color"].value_counts()
    #4 fur_color_count = data.value_counts()
    fur_color_data.columns = ['Color', 'count']

    filedata = pandas.DataFrame({'Fur Color': fur_color_data.index, 'count': fur_color_data.values})
    filedata.to_csv(path_or_buf='fur_color_data.csv')


    # One more option to calculate number
    #2 color_column = data["Primary Fur Color"].tolist()
    #2 gray_num = color_column.count("Gray")
    #2 cinnamon_num = color_column.count("Cinnamon")
    #2 black_num = color_column.count("Black")

    #1 Manual way
    #1 for color in color_column:
    #1     if color == "Gray":
    #1         gray_num += 1
    #1     elif color == "Cinnamon":
    #1         cinnamon_num += 1
    #1     elif color == "Black":
    #1         black_num += 1
    #1 print(gray_num, cinnamon_num, black_num)

if __name__ == '__main__':
    main()