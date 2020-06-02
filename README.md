Linux Semester Project (Fall 2018)

My hypothesis that I tested for this project was that people name their children after popular TV show characters, leading the name to become more popular as the TV show progresses. For this project I used files from the IMDB database from which I took the information about the TV shows I was tracking, and the US Census Bureau data that tracks, by year, how many people are born with each name each year (counting names given 5 times or more).

I first combed through an IMDB file and took only the TV shows, and then, using a file I compiled of the “top TV shows of all time” which was created by scrapping a few websites, took only the TV shows deemed to be a “top TV show.” I then went through a different IMDB file, and created a new file that had each TV show’s relevant information with their character names added. I then reorganized that file so that each character-TV show combination was listed separately, and removed doubles, shows that had the same name as the popular show but were in fact less popular remakes, and names that were not actually names (like Doctor or Admiral). I then found the popularity of each name for each year that the TV show was on TV and the 5 years before that. I then found the slope of the line that represented the popularity of each name-TV show combination before the show was on (s1), and while the show was on (s2). I then made a scatter plot graph representing my findings with s1’s being the x-coordinates and s2’s being the y-coordinates.

My findings show that rather than a TV show influencing parents to name their children after a character, which would have caused a name’s popularity to rise, TV shows more often choose names that are popular when the show begins and then decline or stay stagnant in popularity, showing that TV show names rarely cause a name to rise significantly in popularity. There are a few exceptions, including names that had never been found in the census bureau data previously, but begin to be found once the show begins.

To run, download the necessary files from IMDB and data.gov and run the makefile.

Mori Schick
