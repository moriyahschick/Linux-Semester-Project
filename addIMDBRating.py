#!/usr/bin/env python3

f = open("calculateSlopes.txt")
withSlopes = f.readlines()
f.close()

f2 = open("../IMDB_files/title.ratings.tsv")
IMDBRatings = f2.readlines()
f2.close()

f3 = open("../IMDB_files/title.basics.tsv")
basicInfo = f3.readlines()
f3.close()

f4 = open("characterNamesFirst.txt")
charNamesFirst = f4.readlines()
f4.close()

info = {}                      #key: title, data: tconst
for show in basicInfo:
    fields = show.split("\t")
    tconst = fields[0]
    title = fields[2]     #this is the primary title, originalTitle is in fields[3]
    info[title] = tconst
#print(info)

ratings = {}                   #key: tconst, data: avgRating
for line in IMDBRatings:
    fields = line.split("\t")
    tconst = fields[0].lstrip()
    avgRating = fields[1]
    ratings[tconst] = avgRating
    #print(tconst, ratings[tconst])
#print(ratings)

TVShowName = {}               #key: nameTVShow_combo, data: just title 
for thing in charNamesFirst:
    fields = thing.split("|")
    nameTVShow = fields[4].replace(">", "").replace("\n", "")
    TVShow = fields[3]
    TVShowName[nameTVShow] = TVShow

if "tt6736612" in ratings:
    print("tt6736612 in ratings")
else:
    print("not in ratings")
    
#print(withSlopes)
for x in withSlopes:
    line = x.replace("\n", "")
    fields = line.split("|")
    nameTVShow_combo = fields[0]
    percentage = fields[1]
    #print(len(fields), fields)
    #print(len(fields))

    justTitle = TVShowName[nameTVShow_combo]
    tconst = info[justTitle]
    print(tconst)
    if tconst in ratings:
        avgRating = ratings[tconst]
        #print(justTitle, tconst, avgRating)

    if tconst not in ratings:
        continue
        #print("ERROR: no tconst in ratings for ", justTitle)
    #except: print("ERROR: tconst not found for ", justTitle)
    #if ratings[tconst] == True:
        #print(justTitle, tconst, rating)
    #else:
        #print("ERROR: rating not found for ", justTitle)
    #try: rating = ratings[tconst]
    #except: print("ERROR: rating not found for ", justTitle) 
    #print(justTitle, tconst, rating)

    #print(nameTVShow_combo, percentage, rating)
