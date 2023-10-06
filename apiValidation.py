import json
import requests
from utilities.configurations import getConfig

# sending the get request
# response = requests.get('https://postman-echo.com/get?foo1=bar1&foo2=bar2')
# # response can be read in mulitple ways like text, json etc and use as per your need.
# text_response = response.text
# json_response = response.json()
# print(type(text_response))
# print(type(json_response))
# print(json_response)
#
# assert response.status_code == 200
# assert json_response['headers']['host'] == 'postman-echo.com'
# dict_headers = dict(response.headers)
# assert dict_headers['Content-Type'] == 'application/json; charset=utf-8'

# with open('C:\\Users\\Amit\\PycharmProjects\\backendProject\\data\\requestBodyEcho.json') as f:
#     response_echo = requests.get('https://postman-echo.com/post',
#         headers={'Cookie':'sails.sid=s%3A1rXI3JUaTQGm9Qautm9IRMazJJimeBxR.g4vOrnzsvQ6EiAnbsHOZO%2F%2Bf4PBwHLhc79lnNOKxZ%2BU',
#         'User-Agent':'PostmanRuntime/7.32.3','Content-Type':'application/json'},
#         data=json.load(f))
#     print(type(response_echo))
#     print(response_echo)

# sending the post request
with open('C:\\Users\\Amit\\PycharmProjects\\backendProject\\data\\requestBodyEcho.json') as f:
    response_echo = requests.post(url=getConfig()['API']['endpoint_echo'], json=json.load(f))
    response_output = response_echo.json()

# Validating the response
with open('C:\\Users\\Amit\\PycharmProjects\\backendProject\\data\\requestBodyEcho.json') as f1:
    input_payload = f1.read()
    request_input = json.loads(input_payload)

    # Comparing request & response
    assert request_input == response_output['json'], "IO assertion failed"
    print("IO assertion successful")

    # Other ways to pass message with assert
    # assert request_input == response_output['json'] and not print("IO assertion successful"),"IO assertion failed"
    # def myfunc(msg='assert OK'):
    #     print msg
    #     return True
    #
    # assert self.clnt.stop_io() == 1 and myfunc("IO stop succeeded"), "IO stop failed"

# Cookies management
response_cookies = requests.get('https://httpbin.org/cookies', cookies={'visit-month': "March"})
print(response_cookies.text)
print(response_cookies.status_code)

# another way using sessions
se = requests.session()
se.cookies.update({'visit-month': "July"})

response_cookies1 = se.get('https://httpbin.org/cookies')
print(response_cookies1.history)
print(response_cookies1.text)
print(response_cookies1.status_code)

# timeout can be used to let the request wait for sometime to capture response for heavyload api's
response_timeout = requests.get('https://httpbin.org/cookies', cookies={'visit-month': "March"}, timeout=3)
print(response_timeout.text)
print(response_timeout.status_code)


