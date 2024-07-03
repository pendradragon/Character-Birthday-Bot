from main import base
from datetime import datetime

class dictBasics:
    #used in the actual calendar portion of the code
    calendarDict = dict()

    #add function
    def add(CharacterName, DOB):
        #if the character is in the list of characters
        if CharacterName in base.serverDict:
            print(CharacterName + " is already in the the birthday logs.")
        else:
            base.serverDict[CharacterName] = DOB
            dictBasics.calendarDict[CharacterName] = datetime.strptime(DOB, '%m-%d').date()
            print(CharacterName + " was added to the birthday logs.")

    #remove function
    def remove(CharacterName):
        if CharacterName not in base.serverDict:
            print(CharacterName + " is not in the birthday logs.")
        else:
            base.serverDict.pop(CharacterName)
            dictBasics.calendarDict.pop(CharacterName)
            print(CharacterName + " was removed from the birthday logs")

    #find DOB function
    def findDOB(CharacterName):
        if CharacterName not in base.serverDict:
            print(CharacterName + " could not be found in the birthday logs")
        else:
            print(CharacterName + " was born on " + base.serverDict[CharacterName])
