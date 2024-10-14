from birthdayData import birthdays  

#command to add characters to the global dictionary
def add(name, date):
    birthdays[name] = date

#command to remove the desired command from the global dictionary
def remove(name):
    if name in birthdays:
        del birthdays[name]
        