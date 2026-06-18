import caesar_cipher_art

def caesar(direction,text,shift):
    output_text = ""
    if direction == "decode":
        shift*=-1
    for letter in text:
        if letter not in alphabets:
            output_text += letter
        else:
            index = alphabets.index(letter)
            index += shift
            index %= 26
            output_text += alphabets[index]
    print(f"Here is the {direction}d result :{output_text}")

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']
print(caesar_cipher_art.logo)
while True:
    direction=input("Type encode to encrypt or type decode to decrypt :\n")
    text=input("Enter original text:\n")
    shift=int(input("Enter shift amount :\n"))
    caesar(direction,text,shift)
    play_again=input("Do you want to play again?(y/n):\n")
    if play_again == "n":
        print("Goodbye")
        break






