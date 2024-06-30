from main import base

class dictBasics:
    #add function
    def add(CharacterName, DOB):
        #if the character is in the list of characters
        if CharacterName in base.serverDict:
            print(CharacterName + " is already in the the birthday logs.")
        else:
            base.serverDict[CharacterName] = DOB
            print(CharacterName + " was added to the birthday logs.")

    #remove function
    def remove(CharacterName):
        if CharacterName not in base.serverDict:
            print(CharacterName + " is not in the birthday logs.")
        else:
            base.serverDict.pop(CharacterName)
            print(CharacterName + " was removed from the birthday logs")

    
