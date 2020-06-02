#!/usr/bin/env python3

import re
import urllib.request

#your regex here
symbol_pat = re.compile(r'<h2><a href=.*?>(.*?):', flags=re.DOTALL)

# read the entire page and turn it into a string
#give url
f = urllib.request.urlopen("https://editorial.rottentomatoes.com/guide/100-percent-certified-fresh-tv-seasons/")
data = f.read().decode() 
data = data.split("<div class='col-sm-18 col-full-xs countdown-item-content'>")

if data:
    #print(data[0])
    #found = re.findall(symbol_pat, data)
    for i in range(1, len(data)):
        found = re.findall(symbol_pat, data[i])
        for x in found:
            print(x)


#will get multiple of the same show because different seasons are different listings
#but for the purpose of this project, if 1+ seasons of a show are mentioned
#the entire show will get a listing
#thus the necessary sort | uniq on the command line
