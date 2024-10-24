
with open("./input/hero_name.txt") as name_file:
    names = name_file.readlines()

#print(names)

for name in names:
    with open("./input/EXAMPLE.TXT") as example_file:
        letter = example_file.read()
    new_name = name.strip("\n")
    new_letter = letter.replace("[name]", new_name)

    with open(f"./output/say_hello_to_{new_name}.txt", mode="w") as file:
        file.write(new_letter)