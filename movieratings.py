
movie_titles = ['Beaches', 'Finding Nemo', 'Rear Window', 'Gigli', 'Fiddler on the Roof'] 
parental_rating = ['PG-13', 'G', 'not rated', 'R', 'G']
imdb_rating =  [6.7, 8.2, 8.6, 2.3, 8.0]
genre = [ 'Comedy/Drama/Music', 'Animated/Comedy/Family/Adventure', 'Mystery/Thriller', 'Comedy/Crime/Romance', 'Drama/Family/History/Musical/Romance']
bechdel_rating = [5, 6, 7, 8, 9]

for movie_titles, parental_rating, imdb_rating, genre, bechdel_rating in zip(movie_titles, parental_rating, imdb_rating, genre, bechdel_rating):
	print movie_titles, parental_rating, imdb_rating, genre, bechdel_rating
