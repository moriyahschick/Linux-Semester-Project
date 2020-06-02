#!/usr/bin/env python3

import math

f = open("findSlopeInfo.txt")
slopeInfo = f.readlines()
f.close()

#if wanted to scale, then multiply by 10,000
#by 4 because there are 4 lines for each character/TVshow combinations
for i in range(0, len(slopeInfo)-4, 4):
    s1A = slopeInfo[i]
    s1A_fields = s1A.split("|")
    s1A_nameTVShow = s1A_fields[0]
    s1A_status = s1A_fields[1]
    s1A_year = float(s1A_fields[2])
    s1A_percentage = float(s1A_fields[3].replace("\n", ""))

    s1B = slopeInfo[i+1]
    s1B_fields = s1B.split("|")
    s1B_nameTVShow = s1B_fields[0]
    s1B_status = s1B_fields[1]
    s1B_year = float(s1B_fields[2])
    s1B_percentage = float(s1B_fields[3].replace("\n", ""))

    s2A = slopeInfo[i+2]
    s2A_fields = s2A.split("|")
    s2A_nameTVShow = s2A_fields[0]
    s2A_status = s2A_fields[1]
    s2A_year = float(s2A_fields[2])
    s2A_percentage = float(s2A_fields[3].replace("\n", ""))

    s2B = slopeInfo[i+3]
    s2B_fields = s2B.split("|")
    s2B_nameTVShow = s2B_fields[0]
    s2B_status = s2B_fields[1]
    s2B_year = float(s2B_fields[2])
    s2B_percentage = float(s2B_fields[3].replace("\n", ""))

    #s1 slope = slope of name before TV show
    #s2 slope = slope of name while TV show was/is on

    s1_percentage = float(format(s1B_percentage - s1A_percentage, '.8f'))
    s1_year = float(s1B_year - s1A_year)
    #print(s1_percentage, s1_year)

    s2_percentage = float(format(s2B_percentage - s2A_percentage, '.8f'))
    s2_year = float(s2B_year - s2A_year)
    #print(s2_percentage, s2_year)
    
    #print(s1A_nameTVShow, s1_percentage, s2_percentage)

    #Name was not in census bureau data, so % had been set to 0:
    if ((s1_percentage == 0.0) and s2_percentage == (0.0)) or ((s1_year == 0.0) or (s2_year == 0.0)):
        print(end="")

    else:
        s1_slope = format(float(s1_percentage)/float(s1_year), '.8f')
        s2_slope = format(float(s2_percentage)/float(s2_year), '.8f')
        print(s1A_nameTVShow + "|" + s1_slope + "|" + s2_slope)
     #   if (s1_slope != "0.00000000") and (s1_slope != "-0.00000000"):
      #      try: nameImpactRatio = format(float(s2_slope)/float(s1_slope), '.8f')
       #     except: print("ERROR: division by 0 attempted. ", s1A_nameTVShow, "  s2_slope: ", s2_slope, " s1_slope: ", s1_slope)

        #    if nameImpactRatio != "0.00000000":
                #print(s1A_nameTVShow + "|" + s1_slope + "|" + s2_slope)
                #print(s1A_nameTVShow + "|" + str(nameImpactRatio))
    
