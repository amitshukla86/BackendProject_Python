import random


def birthdayParadox():
    numOfBirthdays = int(input("How many birthdays should I generate?(Max 100)"))
    numOfSimulation = 100000
    dupBirthday = []
    counter = 0
    dup = 0
    run = 0
    listOfListOfBirthdays = []
    print("Here are {} birthdays".format(numOfBirthdays))

    #Generating random birthdays mulitple times
    listOfBirthdays = []
    for m in range(numOfBirthdays):
        month = random.randint(1, 12)
        day = random.randint(1, 31)
        listOfBirthdays.append(str(day) + "-" + str(month))

    print(listOfBirthdays)

    for item2 in listOfBirthdays:
        if listOfBirthdays.count(item2) > 1:
            dup = 1
            dupBirthday.append(item2)
            break

    #This prints if any duplicates found in the list
    if dup == 1:
        print("In this simulation, Multiple people have birthdays on the same day {}".format(dupBirthday))
    else:
        print("There were no two people with same birthday's in above set")

    print("Generating {} random birthdays {} times...".format(numOfBirthdays, numOfSimulation))

    for n in range(numOfSimulation):
        listOfBirthdays = []
        for m in range(numOfBirthdays):
            month = random.randint(1, 12)
            day = random.randint(1, 31)
            listOfBirthdays.append(str(day) + "-" + str(month))
        listOfListOfBirthdays.append(listOfBirthdays)

    input("Press enter to begin...")
    print("Let's run another {} simulations.".format(numOfSimulation))
    print("0 simulation run")
    for item1 in listOfListOfBirthdays:
        for item2 in item1:
            run += 1
            if item1.count(item2) > 1:
                dup = 1
                dupBirthday.append(item2)
                counter += 1
                break

            if run%10000 == 0:
                print("{} simulation run...".format(run))

    percentage = counter/numOfSimulation * 100

    print('''Out of {} simulations of {} people, there was a
matching birthday in that group {} times. This means
that {} people have a {} % chance of
having a matching birthday in their group.
That's probably more than you would think!'''.format(numOfSimulation,numOfBirthdays,counter,numOfBirthdays,percentage))

birthdayParadox()
