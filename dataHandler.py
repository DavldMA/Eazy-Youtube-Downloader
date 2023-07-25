import json
import os
from colorama import Fore, Style

filePath = "config.json"

def saveData(myData):
    with open(filePath, "w") as file:
        json.dump(myData, file)

def readData():
    if os.path.exists(filePath) and os.path.getsize(filePath) > 0:
        with open(filePath, "r") as file:
            loadedData = json.load(file)
            return loadedData
    else:
        newApiKey = input(Fore.GREEN + "Put here you youtube api key: " + Style.RESET_ALL)
        saveData(newApiKey)
        return newApiKey