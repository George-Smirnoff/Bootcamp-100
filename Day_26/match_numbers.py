import pandas as pd
import numpy as np

def open_digits(file):
    return pd.read_csv(file,
                       sep=" ",
                       header=None)

def main():
    file1 = 'file1.txt'
    file2 = 'file2.txt'
    file1_data = [num for num in open_digits(file1)[0]]
    file2_data = [num for num in open_digits(file2)[0]]
    result = [num for num in file1_data if num in file2_data]
    print(result)



if __name__ == '__main__':
    main()