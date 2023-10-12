import time
import datetime


def main():
    while True:
        print("Enter the year for calendar between 0000 to 9999:")
        year = input(">")

        if year.isnumeric():
            if 0000 < int(year) < 10000:
                year = int(year)
                break
        else:
            print("Invalid year entered")

    while True:
        print("Enter month for the calendar between 1 to 12:")
        month = input(">")

        if month.isnumeric():
            if 0 < int(month) < 13:
                month = int(month)
                break
        else:
            print("Invalid month entered")

    calendar = getCalendar(year, month)
    print(calendar)

    miniCal = miniCalendar(year,month)
    print(miniCal)

    filename = "Calendar_" + str(year) + "_" + str(month) + ".txt"
    # with open(filename,'w') as file:


def getCalendar(inpYear, inpMonth):
    MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December')
    calendarText = ""
    calendarText += (' ' * 34) + MONTHS[inpMonth - 1] + ' ' + str(inpYear) + (' ' * 34) + '\n'
    calendarText += "..Sunday....Monday....Tuesday....Wednesday....Thursday....Friday....Saturday..\n"
    weekSeparator = ('+----------' * 7) + '\n'
    blankRow = ('|          ' * 7) + '\n'

    # getting the 1st day of the month & year
    currentDate = datetime.date(inpYear, inpMonth, 1)

    # getting previous sunday from the current date
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        calendarText += weekSeparator

        for n in range(7):
            if currentDate.weekday() == 6:
                calendarText += '|' + str(currentDate.day).rjust(2) + '(h)' + (' ' * 5)
            else:
                calendarText += '|' + str(currentDate.day).rjust(2) + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        calendarText += '\n'

        for n in range(3):
            calendarText += blankRow

        # checking if the month has changed or not
        if currentDate.month != inpMonth:
            break


    calendarText += weekSeparator
    return calendarText

def miniCalendar(year, month):

    MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December')
    currentDate = datetime.date(year,month,1)
    calendarText = 'SunMonTueWedThuFriSat\n'

    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        for n in range(7):
            calendarText += str(currentDate.day).rjust(3)
            currentDate += datetime.timedelta(days=1)
        if currentDate.month != month:
            break
        calendarText += '\n'

    return calendarText
main()