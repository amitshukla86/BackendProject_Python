# This game is used to guess the number between a given range
import random


# With For loop
def guessTheNumber():
    num = int(input("Please guess the number between 1 to 20: "))
    guesses = 6
    randomNum = random.randint(1, 20)
    print(randomNum)

    for i in range(guesses):

        if num > randomNum:
            print("Entered number is greater than number!!")
        elif num < randomNum:
            print("Entered number is less than number!!")
        elif num == randomNum:
            print("You have guessed the number correctly!!")
            break
        else:
            print("Invalid input. Please print number between 1 and 20")

        num = int(input("Please guess the number between 1 to 20 again: "))

        if i == guesses - 1:
            print("You have exceeded the number of guesses. The number was: " + str(randomNum))
            again = input("Do you want to play again(Y/N)?")
            if again == "Y":
                i = 0
            else:
                print("Thanks for playing")


# With While loop
def guessTheNumberWhile():
    guesses = 6
    randomNum = random.randint(1, 20)
    print(randomNum)
    i = 0

    while i < guesses:

        num = int(input("Please guess the number between 1 to 20 again: "))
        if num > randomNum:
            print("Entered number is greater than number!!")
        elif num < randomNum:
            print("Entered number is less than number!!")
        elif num == randomNum:
            print("You have guessed the number correctly!!")
            break
        else:
            print("Invalid input. Please print number between 1 and 20")

        if i == guesses - 1:
            print("You have exceeded the number of guesses. The number was: " + str(randomNum))
            again = input("Do you want to play again(Y/N)?")
            if again == "Y":
                i = 0
            else:
                print("Thanks for playing")
                i += 1
        else:
            i += 1


guessTheNumberWhile()
