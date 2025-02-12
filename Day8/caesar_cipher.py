alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = []
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter not in alphabet:
            output_text.append(letter)
        else:

            output_text.append(alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)])

    print(f"Here is your {direction}d result: ", ''.join(output_text))

caesar(original_text=text, shift_amount=shift, encode_or_decode = direction)

game_on = True
while game_on:
    game_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if game_continue == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(original_text=text, shift_amount=shift, encode_or_decode = direction)
    elif game_continue == "no":
        game_on = False
        print("Goodbye")
    else:
        print("Invalid input.")