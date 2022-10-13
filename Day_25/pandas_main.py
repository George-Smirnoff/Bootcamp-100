import pandas
# import statistics

def f(x):
    x = x * 1.8 + 32
    return float(x)

def main():
    filepath = 'forecast.csv'
    # pandas.set_option('display.max_rows', 4)
    weather = pandas.read_csv(filepath)
    print(weather)

    # Get data in column
    # Call as a key
    avg = weather["temp"].mean()
    # Call as an object
    max = weather.temp.max()
    print(f"Average temperature is {avg}")
    print(f"Max temperature is {max}")

    # temperatures = weather["temp"].to_list()
    # x = statistics.mean(temperatures)
    # print(f"Average temperature is {x}")


    # Get data in row
    row_monday = weather[weather.day == "Monday"]
    print(row_monday)
    print(weather.loc[[4]])
    print(weather.loc[4:4])


    # Get raow with max temprature
    row_max_temp = weather[weather.temp == max].to_string(header=False)
    print(f"The row with max temperature is:\n{row_max_temp}")

    # Convert Celcius to Fahrenheit
    print(row_monday.temp.apply(f))


    # Create Dataframe from scratch
    data_dict = {
        "students": ["Jack", "Amelie", "John"],
        "score": [32, 66, 58]
    }

    dataframe = pandas.DataFrame(data=data_dict)
    print(dataframe)

if __name__ == '__main__':
    main()