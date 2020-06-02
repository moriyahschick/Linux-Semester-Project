all: plot.pdf

clean:
	rm allTVShows.txt IGNtop100.txt InsiderTop50.txt RottenTomatoesList.txt allTopTVShows.txt allTopTVShows_IMDB.txt TVshowsWcharacters.txt cleanCharacterNames.txt characterNamesFirst.txt cleanDoNotPlot.txt calculateSlopes.txt amtPerNamePerYear.txt TVshowsWactors.txt findSlopeInfo.txt plot.pdf small_plot.pdf

#go through movie data with spark, only take TV shows from all media types
allTVShows.txt:
	spark-submit onlyTVshows.py > allTVShows.txt

#scrape a few websites to get the top shows
IGNtop100.txt:
	python3 IGNtop100.py > IGNtop100.txt

InsiderTop50.txt: #InsiderTop50.py
	python3 InsiderTop50.py > InsiderTop50.txt

RottenTomatoesList.txt: #RottenTomatoesList.py
	python3 RottenTomatoesList.py | sort | uniq > RottenTomatoesList.txt

#consolidate everything scraped
allTopTVShows.txt: IGNtop100.txt InsiderTop50.txt RottenTomatoesList.txt
	touch allTopTVShows.txt
	cat IGNtop100.txt >> allTopTVShows.txt
	cat InsiderTop50.txt >> allTopTVShows.txt
	cat RottenTomatoesList.txt >> allTopTVShows.txt

#take only the top TV shows
allTopTVShows_IMDB.txt: allTopTVShows.txt allTVShows.txt
	spark-submit IMDB_topTVshows_SPARK.py > allTopTVShows_IMDB.txt

#add actors
TVshowsWcharacters.txt: allTopTVShows_IMDB.txt
	python3 TVshowsWactors.py > TVshowsWcharacters.txt

#list by character
cleanCharacterNames.txt: TVshowsWcharacters.txt
	python3 cleanCharacterNames.py > cleanCharacterNames.txt

characterNamesFirst.txt: cleanCharacterNames.txt
	python3 characterNamesFirst.py | sort | uniq > characterNamesFirst.txt

cleanDoNotPlot.txt: doNotPlot.txt
	python3 cleanDoNotPlot.py | uniq > cleanDoNotPlot.txt

amtPerNamePerYear.txt: cleanDoNotPlot.txt characterNamesFirst.txt
	python3 amtPerNamePerYearNEW.py > amtPerNamePerYear.txt

findSlopeInfo.txt: amtPerNamePerYear.txt
	python3 findSlopeInfo.py > findSlopeInfo.txt

calculateSlopes.txt: findSlopeInfo.txt
	python3 calculateSlopes.py > calculateSlopes.txt

plot.pdf: calculateSlopes.txt
	./pdfPlot.py
	./smallerPlot.py
