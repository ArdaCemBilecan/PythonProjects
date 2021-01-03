import pandas as pd

films= pd.read_csv("imdb_1000.csv")

#print(films)
print(films.columns)

print(films.head())
print(films["title"].head())
print("---------------------------------")
print(films[:9][["title","star_rating"]])

print("---------------------------------")

filtre1 = films["star_rating"] >=8.5
filtre2=  films["star_rating"]<9.5

print(films[filtre1][["title","star_rating"]])
print("---------------------------------")

print(films[filtre1 & filtre2][["title","star_rating"]])


print("---------------------------------")

print( films.query('star_rating >=8.5 & star_rating<9.5'))  #query ile aynı işlemi yapabilirsin
