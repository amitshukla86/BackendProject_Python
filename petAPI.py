import requests
from utilities.configurations import *
from utilities.commonFunctions import *

# getting working petid
url1 = getConfig()['API']['petstore_endpoint'] + getConfig()['API']['petstoreStatus_resource']
response_petid = requests.get(url1)

pet_list = response_petid.json()
petid = pet_list[0]['id']
assert response_petid.status_code == 200

# Uploading files as part of the request
# url = getConfig()['API']['petstore_endpoint'] + "/pet/" + str(petid) + "/uploadImage"
# print(url)
# file = {'file': open('C:\\Users\\Amit\\PycharmProjects\\backendProject\\Files\\Dog_image.jpg', 'rb')}
# response_petstore = requests.post(url, files=file)
# assert response_petstore.status_code == 200
# print(response_petstore.text)

# Creating user for petstore using an array

url = getConfig()['API']['petstore_endpoint'] + getConfig()['API']['petstoreUserArray_resource']
body = getUsersPayloadFromDB('select * from users')
header = {"accept": "application/json", "Content-Type": "application/json"}
response_petstoreuser = requests.post(url, headers=header, data=body)
print(response_petstoreuser.status_code)
print(response_petstoreuser.text)

# Creating single user for petstore
url = getConfig()['API']['petstore_endpoint'] + getConfig()['API']['petstoreUser_resource']
body = getDictUsersPayloadFromDB('select * from users')
header = {"accept": "application/json", "Content-Type": "application/json"}
print(url, header, body)
response_petstoreuser = requests.post(url, headers=header, data=body)
print(response_petstoreuser.status_code)
print(response_petstoreuser.text)