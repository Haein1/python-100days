import caeser_art

print(caeser_art.logo)


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caeser(text, shift_amount, direction):
    end_text = ""
    for letter in text:
        position = alphabet.index(letter)

        if direction == "encode":
            new_postion = (position + shift_amount) % len(alphabet)
        elif direction == "decode":
            new_postion = (position - shift_amount) % len(alphabet)
        end_text += alphabet[new_postion]

    print(f"The {direction}d text is {end_text}")




option = "yes"
while option == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    option = input("Type 'yes' when you want to conniue. Otherwise type 'no' to quit\n")
    
