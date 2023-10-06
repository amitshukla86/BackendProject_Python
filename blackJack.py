def blackJack():
    hearts = chr(9829)
    spade = chr(9824)
    diamond = chr(9830)
    club = chr(9827)

    print(hearts + spade + diamond + club)
    cardTypeList = [hearts, spade, diamond, club]
    cardNumList = ['A', 'K', 'Q', 'J', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    print("How many players are playing the game?")
    numOfPlayers = input(">")


def printCard(type, num):
    print('''_________
|{}      |
|   {}   |
|      {}|
_________'''.format(num, type, num))


def calculation_logic(numOfPlayers):
    playerList = []
    totalPlayer = {}
    for n in range(numOfPlayers+1):
        playerList.append("Player" + str(n))
        totalPlayer.update({playerList[n]: 0})
    playerList[0] = 'Dealer'
    totalPlayer['Dealer'] = totalPlayer.pop('Player0')

    print(playerList)
    print(totalPlayer)
    return totalPlayer

def drawingCards(numOfPlayers, type, num):

    list = calculation_logic(numOfPlayers).keys()
    #for n in range(numOfPlayers):




calculation_logic(4)
printCard("A", "1")
blackJack()
