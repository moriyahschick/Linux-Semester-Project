#!/usr/bin/env python3

f = open("doNotPlot.txt")
dontPlotList = f.readlines()
f.close()
#for x in dontPlotList:
    #print(x)
for x in dontPlotList:
    x = x.replace("\n", "")
    fields = x.split("|")
    #print(len(fields), x, fields)
    showName = fields[0]
    namePart = fields[1]
    fullName = fields[2]
    year = fields[3]

    print(showName + "|" + namePart + "|" + fullName)

    
