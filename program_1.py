'''importing math's random package'''
import random

'''The names of the perceived heros at the fundraising event'''
heroNameList = ["Blue Eyes White Dragon", "Cyclone Supersuit Carl",
                "Gregorian Gym Man", "Karate Kenny Kid", 
                "Liga Lunar Luchador", "Parking Meter Pyro", 
                "Soiree Senorita de Spyderman", "Weight Wordy Wordsmith"]

'''the method for displaying hero names as well as the money values (hard coded and not real)
in a text format, to be read by a simple display monitor (RED LED light, but doesn't
necessairily but what I had in mind.)'''
def displayNow(heroNameList):
    
    '''Number of minimum dollar amount, interchangeable! but for
    test cases, we start with 5'''
    minimumAmount = 5
    
    '''for loop. for every hero list we will create a random number and then assign it to a hero
    and then print a set sentence with both elements (hero name and dollar amount)'''
    for x in heroNameList:
        currentRandNumber = random.randint(minimumAmount,100)
        print("%s donated $%s dollars!" % (x, currentRandNumber))

'''the method for displaying in the console our heros as well as our cash/money amounts'''
displayNow(heroNameList)

'''This program was written by ANTHONY T'''
