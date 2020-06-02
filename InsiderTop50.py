#!/usr/bin/env python3

import re
import urllib.request

#your regex here
symbol_pat = re.compile(r'data-slide-title="([^(]+)')

# read the entire page and turn it into a string
#give url
f = urllib.request.urlopen("https://www.thisisinsider.com/best-tv-shows-of-all-time-2017-6")
data = f.read().decode() 

if data:
    found = re.findall(symbol_pat, data)
    if found:
        for x in found:
            print(x.replace("&quot;", "").replace("&#039;", "'"))

            
