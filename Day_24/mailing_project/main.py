from jinja2 import Environment, FileSystemLoader

def main():
    names = []
    names_path = 'input/names/invited_names.txt'
    with open(names_path, 'r') as name_file:
        names = name_file.read().splitlines()

    environment = Environment(loader=FileSystemLoader("input/letters/"))
    template = environment.get_template("starting_letter.docx")

    for name in names:
        filename = f"output/ready_to_send/message_{name.lower()}.txt"
        content = template.render(
            name = name
        )
        with open(filename, mode="w", encoding="utf-8") as message:
            message.write(content)
            print(f"... wrote {filename}")


if __name__ == '__main__':
    main()