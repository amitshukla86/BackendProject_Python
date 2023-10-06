import json
import os
import openpyxl

#Creating a new excel workbook
wbObj = openpyxl.Workbook()
os.chdir('C:\\Users\\Amit\\PycharmProjects\\backendProject\\Output')
sheetList = wbObj.sheetnames
wbObj_sheet = wbObj[sheetList[0]]
wbObj_sheet.title = 'cakeData'
wbObj.save('cakeData.xlsx')

with open('C:\\Users\\Amit\\PycharmProjects\\backendProject\\data\\donut.JSON') as file:

    #multiple ways to read a file\
    test_text = file.read()
    # print(test_text)
    # print(type(test_text))

    test_list = json.loads(test_text)
    print(test_list)
    print(type(test_list))

    for n in test_list:
        print(n)
        print(type(n))
    # test_json = json.load(file)
    # print(type(test_json))

    #Getting Column names from the input file
    for item in test_list:
        if type(test_list[item]) == 'list':

            





#converting JSON data to columns

