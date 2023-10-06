import configparser
import mysql.connector
from mysql.connector import Error

from utilities.commonFunctions import *


def getSecrets(key):
    with open('C:\\Users\\Amit\\PycharmProjects\\backendProject\\secrets.txt') as file:

        keys_dict = json.load(file)
        if key in keys_dict:
            value = keys_dict[key]
            return value
        else:
            print("Key not present in the secret file")


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def getConnection():
    try:
        conn = mysql.connector.connect(host=getSecrets('dbhost'), database=getSecrets('database'),
                                       user=getSecrets('dbuser'),
                                       password=getSecrets('dbpassword'))
        if conn.is_connected():
            print("Connection is successful")
            return conn
    except Error as e:
        print(e)


def getQueryOneRow(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row


def getQueryAllRow(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


def getUsersPayloadFromDB(query):
    payload = {}
    row1 = getQueryOneRow(query)
    payload["id"] = row1[0]
    payload["username"] = row1[1]
    payload["firstName"] = row1[2]
    payload["lastName"] = row1[3]
    payload["email"] = row1[4]
    payload["password"] = row1[5]
    payload["phone"] = row1[6]
    payload["userStatus"] = row1[7]
    List = "[" + str(payload) + "]"
    return List

def getDictUsersPayloadFromDB(query):
    payload = {}
    row1 = getQueryOneRow(query)
    payload["id"] = row1[0]
    payload["username"] = row1[1]
    payload["firstName"] = row1[2]
    payload["lastName"] = row1[3]
    payload["email"] = row1[4]
    payload["password"] = row1[5]
    payload["phone"] = row1[6]
    payload["userStatus"] = row1[7]
    return payload
