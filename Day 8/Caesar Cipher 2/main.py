alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def decrypt(cipher_text, shift_amount):
    decoded_text = ""
    for char in cipher_text:
        if char in alphabet:
            shifted_position = (alphabet.index(char) - shift_amount) % 26
            decoded_text += alphabet[shifted_position]
    print(f"Your decoded text is: {decoded_text}")


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")
    return cipher_text

def caesar(direction, original_text, shift_amount):
    if direction == "encode":
        encrypt(original_text, shift_amount)
    elif direction == "decode":
        decrypt(original_text, shift_amount)
    else:
        print(f"Sorry, {direction} is not a valid direction.")


coded = encrypt(original_text=text, shift_amount=shift)

decrypt(coded, shift_amount=shift)





