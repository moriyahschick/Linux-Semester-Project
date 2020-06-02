#!/usr/bin/env python3

import re
import subprocess
import sys

#all top TV shows with tconst num
f1 = open("allTopTVShows_IMDB.txt")
a = f1.readlines()
f1.close()


#all TV shows with characters in field[5], TV shows have 1 line per character
f2 = open("title.principals.tsv")
y = f2.readlines()
f2.close()


global showWCharacters
showWCharacters = {}         #will have ALL TV shows in this list

for i in range(len(y)):
    fields = y[i].split("\t")
    tconst = fields[0]
    character = [fields[5]]

    if (character != r'(\N)') and (character != r'(\\N)'):

        if tconst in showWCharacters:
            showWCharacters[tconst].append(character)

        if tconst not in showWCharacters:
            showWCharacters[tconst] = [character]
        
fout = open("TVshowsWactors.txt", "w")

#for each TV show in the txt file of all top shows with tconst num from IMDB
for TVshow in a:
    tconst = TVshow.split("|")[0]        #only part we care about from top TV show file

    if tconst in showWCharacters:
        characters = showWCharacters[tconst]
        print(tconst + "|", end="", file=fout)
        for x in characters:
            print(str(x) + ",", end="", file=fout)
    print(file=fout)
    
fout.close()

f3 = open("TVshowsWactors.txt")
z = f3.readlines()
f3.close()        
    
#print("len of a:", len(a))
#print(a)
for i in range(len(z)):
    #x[i].split -- tconst, name, start year, end year
    #z[i].split -- tconst, characters
    a[i] = a[i].replace("\n", "")
    z[i] = z[i].replace("\n", "")

    fieldsA = a[i].split("|")
    fieldsZ = z[i].split("|")

    tconstA = fieldsA[0]
    tconstZ = fieldsZ[0]

    if tconstA != tconstZ:
        print("ERROR: tconstA != tconstZ !! tconstA = ", tconstA, " tconstZ = ", tconstZ)

    
    if tconstA == tconstZ:
        characters = fieldsZ[1]
        characters = characters.replace("[", "")
        characters = characters.replace("]", "")
        characters = characters.replace("'", "")
        characters = characters.replace("\"", "")
        characters = characters.replace("\n", "")

        #print(a[i])
        print(a[i] + "|" + characters)
