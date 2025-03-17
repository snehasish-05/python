
import art
print(art.logo)

def decrypt(original_text,shift_number):

    srt = ""
    for i in original_text:
        srt += chr(ord(i) - shift_number)

    print(f"Here is the decoded result: {srt}")


def encrypt(original_text,shift_number):

    srt = ""
    for i in original_text:
        srt += chr(ord(i)+shift_number)

    print(f"Here is the encoded result: {srt}")



def caesar(direction_):
    if direction_ == "encode":
        encrypt(text,shift)
    else:
        decrypt(text,shift)









should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction)
    cont = input("Do you want to continue 'y' or 'n'\n").lower()

    if cont == 'n':
        should_continue = False





