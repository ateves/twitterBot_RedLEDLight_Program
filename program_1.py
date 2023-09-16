import random

heroNameList = ["Blue Eyes White Dragon", "Cyclone Supersuit Carl", "Gregorian Gym Man", "Karate Kenny Kid", "Liga Lunar Luchador", "Parking Meter Pyro", "Soiree Senorita de Spyderman", "Weight Wordy Wordsmith"]

def displayNow(heroNameList):
    
    minimumAmount = 5
    
    for x in heroNameList:
        currentRandNumber = random.randint(minimumAmount,100)
        print("%s donated $%s dollars!" % (x, currentRandNumber))

displayNow(heroNameList)
#Code written by ANTHONY T
