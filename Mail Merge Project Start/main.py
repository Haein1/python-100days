#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


names_file = open("./Input/Names/invited_names.txt", "r")
names = names_file.readlines()
#print(names)  ['Aang\n', 'Zuko\n', 'Appa\n', 'Katara\n', 'Sokka\n', 'Momo\n', 'Uncle Iroh\n', 'Toph']

starting_letter_file = open("./Input/Letters/starting_letter.txt", "r")
starting_letter = starting_letter_file.read()
#print(starting_letter)

for name in names:
    new_name = name.strip("\n")
    #print(new_name)
    letter = starting_letter.replace("[Name]", new_name)
    #print(letter)
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as file:
        file.write(letter)

