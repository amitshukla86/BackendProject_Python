

def main():

    while True:
        print("Do you want to encrypt(e) or decrypt(d)?")
        option = input(">").lower()
        if option == 'e' or option == 'd':
            break
        else:
            print("Invalid option selected.")

    while True:
        print("Please enter the key(0 to 25) to use")
        key = input(">")
        if not key.isnumeric():
            print("Invalid key selected.")
        elif 0 <= int(key) < 26:
            break
        else:
            print("Invalid key selected.")

    if option == 'e':
        print("Enter the message you want to encrypt")
        message = input(">")
        encryptMessage = encrypt(message,key)
        print("Encrypted message is: " + encryptMessage)
    elif option == 'd':
        print("Enter the message you want to decrypt")
        message = input(">")
        decryptMessage = decrypt(message, key)
        print("Decrypted message is: " + decryptMessage)


def encrypt(message, key):
    letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
        , 'u', 'v', 'w', 'x', 'y', 'z']
    newMessage = ""

    for letter in message:

        if letter == ' ':
            newMessage += " "
        else:
            index = letterList.index(letter.lower()) + int(key)
            if index > 26:
                index = index - 26

        newMessage += letterList[index]
        #print(newMessage)

    return newMessage

encrypt("hello", 26)

def decrypt(message, key):
    letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
        , 'u', 'v', 'w', 'x', 'y', 'z']
    newMessage = ""

    for letter in message:

        index = letterList.index(letter) - int(key)
        if index < 0:
            index = index + 26
        newMessage += letterList[index]
        #print(newMessage)
    return newMessage

main()