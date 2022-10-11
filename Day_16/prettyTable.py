from prettytable import PrettyTable

def main():
    table = PrettyTable()
    table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electric", "Water", "Fire "])
    print(table.align)
    table.align = "l"
    print(table)


if __name__ == '__main__':
    main()