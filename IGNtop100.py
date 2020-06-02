#!/usr/bin/env python3

import re
import urllib.request

#your regex here
symbol_pat = re.compile(r'data-superscript="0">(.*?)</span>', flags=re.DOTALL)

# read the entire page and turn it into a string
#give url
f = urllib.request.urlopen("https://www.ign.com/lists/top-100-tv-shows/66")
data = f.read().decode() 

if data:
    found = re.findall(symbol_pat, data)
    if found:
        for x in found:
            print(x.strip())
