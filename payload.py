import json
def inputPayload(payloadName,type):
    with open('C:\\Users\\Amit\\PycharmProjects\\backendProject\\data\\' + payloadName) as payloadFile:
        if type=="json" or type=="JSON":
            fileRead = payloadFile.read()
            inputPayload = json.loads(fileRead)
        elif type=="text" or type=="TEXT":
            inputPayload = payloadFile.read()
        else:
            print("Incorrect type passed in the method")

    print(inputPayload)
    return inputPayload

inputPayload('donut.json','json')
inputPayload('requestBodyEcho.json','json')