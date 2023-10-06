import random


def blackJack():
    hearts = chr(9829)
    spade = chr(9824)
    diamond = chr(9830)
    club = chr(9827)
    dealerList = []
    playerList = []

    # Creating a list of card types and all different cards in a deck
    cardTypeList = [hearts, spade, diamond, club]
    cardNumList = ['A', 'K', 'Q', 'J', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    # Drawing the first card for the dealer and 2 cards for the player
    dealerList.append(random.choice(cardTypeList) + "-" + random.choice(cardNumList))
    playerList.append(random.choice(cardTypeList) + "-" + random.choice(cardNumList))
    playerList.append(random.choice(cardTypeList) + "-" + random.choice(cardNumList))

    # Summing the value of the cards
    dealerTotal = summation(dealerList)
    playerTotal = summation(playerList)

    # Printing the cards and total
    print("Dealer: " + str(dealerTotal))
    printCard(dealerList)
    print("Player: " + str(playerTotal))
    printCard(playerList)

    print("Do you want hit(h) or stand(s)")
    response = input(">")

    while response.lower() != 'h' and response.lower() != 's':
        print("Please enter a valid input from either h or s")
        response = input(">")

    while response.lower() == 'h':
        # assigning another card to the player and printing it
        playerList.append(random.choice(cardTypeList) + "-" + random.choice(cardNumList))
        playerTotal = summation(playerList)
        print("Player: " + str(playerTotal))
        printCard(playerList)

        if playerTotal > 21:
            print("You are bust. Dealer WINS")
            break
        elif playerTotal == 21:
            print("Its blackJack. You WIN")
            break
        # Checking if user wants to hit again or stand
        print("Do you want hit(h) or stand(s)")
        response = input(">")

    if response.lower() == 's':
        print("Player: " + str(playerTotal))
        dealerTotal = dealarPlay(dealerList, cardTypeList, cardNumList)
        print("Dealer: " + str(dealerTotal))
        printCard(dealerList)

        if dealerTotal > 21:
            print("Dealer is bust. You WIN")
        elif dealerTotal > playerTotal:
            print("Dealer WINS")
        elif dealerTotal == playerTotal:
            print("Its a draw")
        else:
            print("You WIN")


# Function to print the card for the players
def printCard(list):
    for item in list:
        x = item.split("-")[0]
        y = item.split("-")[1]
        print('''_________
|{}      |
|   {}   |
|      {}|
_________'''.format(y, x, y))


# Function to sum the total of all hands that the user has
def summation(cardList):
    total = 0
    for item in cardList:
        n = item.split("-")[1]
        if n == 'K' or n == 'Q' or n == 'J':
            n = 10
            total = total + n
        elif n == 'A' and total < 11:
            n = 11
            total = total + n
        elif n == 'A' and total > 10:
            n = 1
            total = total + n
        else:
            total = total + int(n)
    return total


def dealarPlay(list, cardTypeList, cardNumList):
    list.append(random.choice(cardTypeList) + "-" + random.choice(cardNumList))
    Total = summation(list)

    while Total < 17:
        list.append(random.choice(cardTypeList) + "-" + random.choice(cardNumList))
        Total = summation(list)

    return Total


blackJack()

