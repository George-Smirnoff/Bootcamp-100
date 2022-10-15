import pandas

def main():
    student_dict = {
        "student": ["Angela", "James", "Lily"],
        "score": [56, 76, 98]
    }

    student_dataframe = pandas.DataFrame(student_dict)
    print(student_dataframe)

    # for (key,value) in student_dataframe.items():
    #     print(f"Key is {key}\n")
    #     print(value)


    for key, row in student_dataframe.iterrows():
        print(f"\nKey is {key}")
        print(row)
        print(row.student, row.score)

if __name__ == '__main__':
    main()