import pyspark
import sys

f = open("allTopTVShows.txt")
TVshows = f.readlines()
TVshowNames = []
for x in TVshows:
    TVshowNames.append(x.replace("\n", ""))
f.close()
    

def ifTopShow(x):
    fields = x.split("|")

    tconst = fields[0]
    titleName = fields[1]
    startYear = fields[2]
    endYear = fields[3]

    if titleName in TVshowNames:
        print("yes")
        return x

    

sc = pyspark.SparkContext()
sc.setLogLevel("ERROR")

a = sc.textFile("allTVShows.txt")\
      .filter(lambda x: x.split("|")[1] in TVshowNames)\
      .collect()

for show in a:
    print(show)
#.saveAsTextFile("IMDB_top_TV_shows")

