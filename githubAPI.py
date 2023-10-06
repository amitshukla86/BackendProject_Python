import requests

from utilities.commonFunctions import *
from utilities.configurations import getConfig

classObj = commonFunc()

print(getSecrets('username'), getSecrets('password'))
# se = requests.session()
# se.auth = auth = (classObj.getSecrets('username'), classObj.getSecrets('password'))
# print(getConfig()['API']['github_endpoint'] + getConfig()['API']['github_user_resource'])
#
# response_github = se.get(url=getConfig()['API']['github_endpoint'] + getConfig()['API']['github_user_resource'])
# print(response_github.text)
# print(response_github.status_code)
#
# response_github1 = se.get(url=getConfig()['API']['github_endpoint'] + getConfig()['API']['github_repos_resource'])
# print(response_github1.text)
# print(response_github1.status_code)


