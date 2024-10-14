from birthdayData import birthdays  

#command to add characters to the global dictionary
def add(name, date):
    birthdays[name] = date

#command to remove the desired command from the global dictionary
def remove(name):
    if name in birthdays:
        del birthdays[name]

#searching commands
def getDOB(character):
    return birthdays.get(character)

def get_character_by_DOB(date):
    return [name for name, dob in birthdays.items() if dob == date]