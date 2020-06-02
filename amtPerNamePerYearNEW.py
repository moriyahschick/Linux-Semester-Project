#!/usr/bin/env python3

import math

totalAmtInYear = {}

for i in range(1945, 2018):
    fileName = "/home/mschick/linuxProject/names_national_by_year/yob" + str(i) + ".txt"
    f1 = open(fileName)
    nameGenderAmt = f1.readlines()
    f1.close()
    
    yearTotal = 0
    for line in nameGenderAmt:
        fields = line.split(",")
        name = fields[0]
        gender = fields[1]
        amount = int(fields[2])

        yearTotal += amount

    totalAmtInYear[i] = yearTotal

#print(totalAmtInYear)

nameYearAmt = {}

for i in range(1945, 2018):
    fileName = "/home/mschick/linuxProject/names_national_by_year/yob" + str(i) + ".txt"
    f2 = open(fileName)
    nameGenderAmt2 = f2.readlines()
    f2.close()

    for line in nameGenderAmt2:
        fields = line.split(",")
        name = fields[0]
        gender = fields[1]
        amount = int(fields[2])

        year = i
        totalAmount = totalAmtInYear[year]

        percentOfTotal = format(amount/totalAmount, '.8f')

        #print(name, amount, totalAmount, percentOfTotal)

        nameYear = name + str(i)
        nameYearAmt[nameYear] = percentOfTotal

f3 = open("characterNamesFirst.txt")
characterNames = f3.readlines()
f3.close()

#print(characterNames)

f4 = open("cleanDoNotPlot.txt")
doNot = f4.readlines()
f4.close()
doNotPlot = []
for thing in doNot:
    thing = thing.replace("\n", "")
    doNotPlot.append(thing)

for x in characterNames:
    fields = x.split("|")
    characterName = fields[0]
    showName = fields[3]
    fullName = fields[4].split(">")[0]

    try: startYear = int(fields[1])
    except: print("ERROR: invalid start year for ", showName)
    try: endYear = int(fields[2])
    except: print("ERROR: invalid end year for ", showName)

    for i in range(startYear-5, endYear+1):
        year = str(i)
        starting = False
        if int(year) == startYear:
            starting = True
        nameYear = characterName + year

        if nameYear in nameYearAmt:
            percent = nameYearAmt[nameYear]
            printLine = showName + "|" + characterName + "|" + fullName
            if printLine not in doNotPlot:
                print(characterName + showName + "|" + year + "|" + str(starting) + "|" + percent)
        if nameYear not in nameYearAmt:
            print(end="")
            #percent = str(0.00000000)
            #printLine = showName + "|" + characterName + "|" + fullName
            #if printLine not in doNotPlot:
                #print(characterName + showName + "|" + year + "|" + str(starting) + "|" + percent + "not in nameYearAmt")
