# This program contains the tic tac toe game that can be played between 2 players
import random


def printTicTacToe(dataDict):
    print(dataDict["top-l"] + " | " + dataDict["top-m"] + " | " + dataDict["top-r"])
    print("-------")
    print(dataDict["mid-l"] + " | " + dataDict["mid-m"] + " | " + dataDict["mid-r"])
    print("-------")
    print(dataDict["bot-l"] + " | " + dataDict["bot-m"] + " | " + dataDict["bot-r"])


def ticTacToe():
    # Dictionary with empty values
    dict = {"top-l": "", "top-m": "", "top-r": "", "mid-l": "", "mid-m": "", "mid-r": "", "bot-l": "", "bot-m": "",
            "bot-r": ""}
    i = 0
    dict1 = {}
    winner = ""
    comp = ""

    # Getting input from the user between X and O
    choice = input("Choose between X or O: ").upper()
    if choice == "X" or choice == "O":
        if choice == "X":
            comp = "O"
        else:
            comp = "X"
    else:
        print("Enter a valid input. X or O")

    #Taking input from the user to put the X or O on the board
    while i < len(dict):
        input1 = input("Select the place where to place the " + choice)
        print("input1 = " + input1)
        if dict[input1] == "":
            dict[input1] = choice
        else:
            input1 = input("Already Filled. Select the place again where to place the " + choice)
        print("input1 = " + input1)
        # if any([bool(dict['name']) == False for r in list]):
        #     print('at least one')

        #Creating dictionary for the empty items
        for d in dict:
            if dict[d] == "":
                dict1[d] = ""
        #Assigning value to random item in the dictionary
        dict[random.choice(list(dict1.keys()))] = comp

        # compInput = random.choice()
        printTicTacToe(dict)

        #Checking if anyone won
        if dict["top-r"] == "X" and dict["top-m"] == "X" and dict["top-l"] == "X":
            winner = "X"
            break
        elif dict["mid-r"] == "X" and dict["mid-m"] == "X" and dict["mid-l"] == "X":
            winner = "X"
            break
        elif dict["bot-r"] == "X" and dict["bot-m"] == "X" and dict["bot-l"] == "X":
            winner = "X"
            break
        elif dict["top-r"] == "X" and dict["mid-m"] == "X" and dict["bot-l"] == "X":
            winner = "X"
            break
        elif dict["top-l"] == "X" and dict["mid-m"] == "X" and dict["bot-r"] == "X":
            winner = "X"
            break
        elif dict["top-l"] == "X" and dict["mid-l"] == "X" and dict["bot-l"] == "X":
            winner = "X"
            break
        elif dict["top-m"] == "X" and dict["mid-m"] == "X" and dict["bot-m"] == "X":
            winner = "X"
            break
        elif dict["top-r"] == "X" and dict["mid-r"] == "X" and dict["bot-r"] == "X":
            winner = "X"
            break
        elif dict["top-r"] == "O" and dict["top-m"] == "O" and dict["top-l"] == "O":
            winner = "O"
            break
        elif dict["mid-r"] == "O" and dict["mid-m"] == "O" and dict["mid-l"] == "O":
            winner = "O"
            break
        elif dict["bot-r"] == "O" and dict["bot-m"] == "O" and dict["bot-l"] == "O":
            winner = "O"
            break
        elif dict["top-r"] == "O" and dict["mid-m"] == "O" and dict["bot-l"] == "O":
            winner = "O"
            break
        elif dict["top-l"] == "O" and dict["mid-m"] == "O" and dict["bot-r"] == "O":
            winner = "O"
            break
        elif dict["top-l"] == "O" and dict["mid-l"] == "O" and dict["bot-l"] == "O":
            winner = "O"
            break
        elif dict["top-m"] == "O" and dict["mid-m"] == "O" and dict["bot-m"] == "O":
            winner = "O"
            break
        elif dict["top-r"] == "O" and dict["mid-r"] == "O" and dict["bot-r"] == "O":
            winner = "O"
            break
        else:
            continue

    if winner == choice:
        print("User is the winner")
    else:
        print("Computer is the winner")


ticTacToe()
