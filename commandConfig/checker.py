from time import sleep
from datetime import datetime, timedelta

#local importation
from main import base
from dictCommands import dictBasics

def printString(date):
    character = dictBasics.calendarDict.keys()[dictBasics.calendarDict.values().index(date)]
    print()

class looper:
    sleepTime = 86400

    def checkDays():
        while True:
            today = datetime.now()
            for possibleDays in dictBasics.calendarDict.values():
                if possibleDays == today:
                    print(printString((possibleDays)))
                    break
            
            sleep(looper.sleepTime)
