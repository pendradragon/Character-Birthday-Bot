Intended Use: For roleplay servers to use and keep their character's birthdays stored

Attributes:
    - Keeps a record of characters birthdays that can be accessed at any time
    - Publishes updates each time it is a character's birthday with a message unique to that server


Available Commands:
 - add(name: string, date: string)
       - Adds the character with the desired birthday to the dictionary that the bot searches
       - SHOULD ONLY USE THE CHARACTERS FIRST NAME
   
 - remove(name: string)
       - Removes the desired character from the search dictionary


 - findDOB(name: string)
       - Finds the specified character's DOB

 - findByDOB(DOB: string)
        - Finds the name of the character with the speficied DOB

 - setMessage(message: string)
       - Sets the message that is sent every time it is a character's birthday
       - MAKE SURE TO INCLUDE THE STRING {name} IN THE MESSAGE

 - setChannel
       - Sets the CURRENT channel as the one that the birthday reminders are going to be sent to 
