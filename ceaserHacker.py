

def main():
    print("Enter the excrypted ceaser cipher message to decrypt")
    letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
        , 'u', 'v', 'w', 'x', 'y', 'z']
    message = input(">").lower()

    for key in range(0,25):

        newMessage = ""
        for letter in message:

            if letter == ' ':
                newMessage += letter
                continue

            index = letterList.index(letter) + key

            if index > 25:
                index = index - 26
            newMessage += letterList[index]
        print("Key #{}: ".format(key) + newMessage)

main()
