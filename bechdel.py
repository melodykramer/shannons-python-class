# Exercise: Using your first API

# API documentation: http://bechdeltest.com/api/v1/doc

import requests


title = raw_input("What movie would you like to check?")

#Are you putting in a IMDB Number?

try:
    y = int(title)

#what is the bechdel test rating for this IMDB number?

    response = requests.get('http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid='+title).json()

#what is the Open Movie Database info for this IMDB number?

    responseOMDB = requests.get('http://www.omdbapi.com/?i='+title).json()

    print response

    print responseOMDB



#Are you putting in a title? 

except:

#fixes problems with the word The starting movies

    if title[0:3].lower() =='the':
            title = title.replace('The','')

    response = requests.get('http://bechdeltest.com/api/v1/getMoviesByTitle?title='+title).json()

    responseOMDB = requests.get('http://www.omdbapi.com/?t='+title).json()


    print response 

    print responseOMDB

    for movie in response:
        if len(movie) == 0:
            print "Sorry, this isn't in the database"
        print movie




