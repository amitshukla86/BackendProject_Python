import requests

from utilities.configurations import *

addbooks_url = getConfig()['API']['library_endpoint']+getConfig()['API']['library_addbook']
input_payload = {

"name":"Learn Appium Automation with Java",
"isbn":"abcdef",
"aisle":"3323",
"author":"Amit Shukla"
}

response_addbooks = requests.post(addbooks_url,data=input_payload)
response_text = response_addbooks.text
print(response_text)
print(type(response_text))
