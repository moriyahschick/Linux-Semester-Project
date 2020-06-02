#!/usr/bin/env python3

import math

f = open("amtPerNamePerYear.txt")
nameYearPercentage = f.readlines()
f.close()

# To find slope : rise/run
# x-axis : year    y-axis: percentage
# so, slope = percentage/year

for i in range(len(nameYearPercentage)-1):
    fields = nameYearPercentage[i].split("|")
    nameShow = fields[0]
    year = fields[1]
    startingYear = fields[2]
    percentage = fields[3].replace("\n", "")

    prev_fields = nameYearPercentage[i-1].split("|")
    prev_nameShow = prev_fields[0]
    prev_year = prev_fields[1]
    prev_startingYear = prev_fields[2]
    prev_percentage = prev_fields[3].replace("\n", "")
    
    next_fields = nameYearPercentage[i+1].split("|")
    next_nameShow = next_fields[0]                                           
    next_year = next_fields[1]
    next_startingYear = next_fields[2]
    next_percentage = next_fields[3].replace("\n", "")
    
    #want to find s1 - slope of line for name for the 5 years before the show started, and s2 - slope of line for name while the show is on

    #must be info for startYear-5
    if nameShow != prev_nameShow:
        print(nameShow + "|" + "s1A" + "|" + year + "|" + percentage)
              

    else:    #aka nameShow == prev_nameShow
        #must be info for year right before show started
        if next_startingYear == "True":
            print(nameShow + "|" + "s1B" + "|" + year + "|" + percentage)
            

        #must be info for first year of show
        if startingYear == "True":
            print(nameShow + "|" + "s2A" + "|" + year + "|" + percentage)
            

        #must be info for last year of show
        if nameShow != next_nameShow:
            #because there is no census date for 2018, would say percent = 0
            if year != "2018":
                print(nameShow + "|" + "s2B" + "|" + year + "|" + percentage)
            
            else:
                print(nameShow + "|" + "s2B" + "|" + prev_year + "|" + prev_percentage)
                
lastLine = nameYearPercentage[-1]
fields = lastLine.split("|")
nameShow = fields[0]
year = fields[1]
startingYear = fields[2]
percentage = fields[3].replace("\n", "")

secondToLastLine = nameYearPercentage[-2]
fields2 = secondToLastLine.split("|")
prev_year = fields2[1]
prev_percentage = fields2[3].replace("\n", "")


if year != "2018":
    print(nameShow + "|" + "s2B" + "|" + year + "|" + percentage)
else:
    print(nameShow + "|" + "s2B" + "|" + prev_year + "|" + prev_percentage)
