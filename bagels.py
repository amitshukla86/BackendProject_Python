import random

#Creating bagels program which is a 3 digit guessing game and provides hint whether the any number is present in the list of not
def bagels():

    num_digits = 3
    num_guesses = 10

    print('''I am thinking of a {}-digit number. Try to guess what it is.
    Here are some clues:
    When I say: That means:
    Pico - One digit is correct but in the wrong position.
    Fermi - One digit is correct and in the right position.
    Bagels - No digit is correct.'''.format(num_digits))

    number = random.randint(100,999)

    #multiple ways to convert number into a list
    numList = [int(x) for x in str(number)]
    #numList1 = list(map(int,str(number)))
    print(numList)
    print("I have thought up a number.")
    print("You have {} guesses to get it.".format(num_guesses))

    for i in range(num_guesses-1):
        guessNum = int(input("Guess # " + str(i+1)))

        if not str(guessNum).isnumeric():
            print("Please enter an integer")
            continue
        elif len(str(guessNum)) != 3:
            print("Please enter 3 digit integer")
            continue
        elif guessNum < 100 or guessNum > 999:
            print("Please enter number between 100 & 999 both inclusive")
            continue
        elif str(guessNum).strip() == '':
            print("Please enter a valid number")

        guessNumList = [int(x) for x in str(guessNum)]
        print(guessNumList)
        for n in range(len(guessNumList)-1):
            if guessNumList[n] == numList[n]:
                print("Fermi")
            elif guessNumList[n] in numList:
                print("Pico")
            else:
                print("bagels")

bagels()