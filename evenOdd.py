import random


def evenOddGame():
    money = 5000
    even = [2, 4, 6, 8, 10, 12]
    print('''In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.''')

    while True:
        win = 0
        loose = 0

        while True:
            print("You have {} Rupees. How much do you want to bet(or QUIT)".format(money))
            bet = input(">")

            if bet.upper() == "QUIT":
                break
            elif not bet.isnumeric():
                print("Invalid bet entered")
            elif 0 < int(bet) <= money:
                break
            else:
                print("Invalid bet entered")

        if bet.upper() == 'QUIT':
            print("Thanks for playing")
            break
        else:
            bet = int(bet)

        print('''The dealer swirls the cup and you hear the rattle of dice.
The dealer slams the cup on the floor, still covering the
dice and asks for your bet.
 CHO (even) or HAN (odd)?''')
        while True:
            choice = input(">")

            if not choice.isdecimal():
                if choice.upper() == 'CHO' or choice.upper() == 'HAN':
                    choice = choice.upper()
                    break
                else:
                    print("Please enter valid option. CHO or HAN")
            else:
                print("Please enter valid option. CHO or HAN")

        # Generating random number for each dice
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        sum = dice1 + dice2

        print('''The dealer lifts the cup to reveal:
    GO - GO
    {} - {}'''.format(dice1, dice2))
        if sum in even:
            if choice == 'CHO':
                print("You won! You take {} rupees.".format(bet * 2))
                print("The house collects a {} rupees fee.".format(bet / 10))
                win = 1
            else:
                print("You Loose!")
                print("The house collects a {} rupees fee.".format(bet / 10))
                loose = 1
        else:
            if choice == "HAN":
                print("You won! You take {} rupees.".format(bet * 2))
                print("The house collects a {} rupees fee.".format(bet / 10))
                win = 1
            else:
                print("You Loose!")
                print("The house collects a {} rupees fee.".format(bet / 10))
                loose = 1

        if win == 1:
            money = money + (bet*2) - (bet/10)
        elif loose == 1:
            money = money - bet - (bet/10)

evenOddGame()
