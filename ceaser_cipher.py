
#ASCII chars for A-Z: #65-90 and a-z: 97-122
#ASCII chars can be obtained by ord(char) and can be retireved by chr(char)
#Check if the input is alphabet by .isalpha() if not, no need to encrypt it. Just append it to the string
#Get the Base number of A or a according to the uppercase or lowercase of the given input.
#This allows to keep the inputs within the range of it's respective cases.

#Issues: Sometimes, if the shift number is big, it will result in a ASCII chracters that is not printable, this can be checked by .isprintable()

def caesar_cipher(text, shift, process):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            ascii_code = ord(char) 
            base = ord('A') if char.isupper() else ord('a')
            if process == "Encrypt":
                shifted_code = (ascii_code - base + shift) % 26 + base
            elif process == "Decrypt":
                shifted_code = (ascii_code - base -  shift) % 26 + base
            encrypted_char = chr(shifted_code)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

plaintext = input("Your Text: ")
shift = int(input("Shift Number: "))
process = input("Encrypt/Decrypt?: ")
final_text = caesar_cipher(plaintext, shift, process)
print("Text:", final_text)
