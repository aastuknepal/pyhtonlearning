
placeholder = "[name]"

with open("names.txt") as file:
    name = file.readlines()
    print(name)

with open("letter.txt") as letter_file:
    letter_contents= letter_file.read()
    for names in name:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(placeholder, stripped_name)
        print(new_letter)
        with open(f"{stripped_name}.txt", mode="w") as completed:
            completed.write(new_letter)


