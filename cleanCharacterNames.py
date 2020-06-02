#!/usr/bin/env python3

f = open("TVshowsWcharacters.txt")
TVshowFullInfo = f.readlines()
f.close()

for showInfo in TVshowFullInfo:
    showInfo = showInfo.replace("\\n", "")
    showInfo = showInfo.replace("\\", "\'")
    if showInfo[:1] == "\\" or showInfo[-1:] == "\\":
        showInfo = showInfo.replace("\\", "'")        
    print(showInfo)
