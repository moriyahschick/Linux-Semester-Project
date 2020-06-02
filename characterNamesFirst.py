#!/usr/bin/env python3
        
#import re
#import subprocess
#import sys

#all top TV shows with tconst num
f1 = open("cleanCharacterNames.txt")
a = f1.readlines()
f1.close()

#global showWCharacters
f2 = open("notNameTag.txt")
taggedList = f2.readlines()
notAName = []
for x in taggedList:
    line = x.replace("\n", "")
    notAName.append(line)
f2.close()

for TVshow in a:
    fields = TVshow.split("|")
    #print("len of fields: ", len(fields))

    if len(fields) > 1:
        tconst = fields[0]
        showName = fields[1]
        startYear = int(fields[2])
        endYear = fields[3]
        characters = fields[4]

        #characters is a list of the character's names
        characters = characters.split(",")

        for name in characters:
            #years will be the years for which you want to get the percentage for that name
            #so, startYear-5 because we want to get name data starting then
            fullName = name           #ex: Freddie Muller
            name = name.split()       #ex: split Freddie Muller into Freddie and Muller
            #nameShowID = name + ">" + showName    #Freddie Muller>The Honeymooners

            for namePart in name:
                if namePart not in notAName:
                    nameShowID = namePart + ">" + showName    #Freddie Muller>The Honeymooners
                    print(namePart + "|" + str(startYear-5) + "|" + endYear + "|" + showName + "|" + nameShowID)
    

#fout.close()
