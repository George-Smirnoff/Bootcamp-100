
def main():
    # Filter and increase numbers
    numbers = [10, 2, 13, 4, 9]
    new_list = [n + 1 for n in numbers if n <= 10]
    print(new_list)

    # Split String
    name = 'Angela'
    new_name = [letter for letter in name]
    print(new_name)

    # Double range
    duble_range = [n * 2 for n in range(1, 5)]
    print(duble_range)

    # Upper long names
    names_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanore", "Freddie"]
    cap_names = [item.upper() for item in names_list if len(item) > 5]
    print(cap_names)

if __name__ == '__main__':
    main()