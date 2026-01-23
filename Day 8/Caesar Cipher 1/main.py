alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_word = ""
    for letter in original_text:
        if letter not in alphabet:
            continue
        index = alphabet.index(letter)
        new_index = index + shift_amount
        if new_index > len(alphabet):
            new_index = abs(new_index - len(alphabet))
            encrypted_word += alphabet[new_index]
        else:
            encrypted_word += alphabet[new_index]
    return encrypted_word

encrypted_text = encrypt(text, shift)

print(encrypted_text)






# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

