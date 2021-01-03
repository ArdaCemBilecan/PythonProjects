import pandas as pd

films = pd.read_csv("imdb_1000.csv")

print(films.head())

print(films["star_rating"].mean())


print(films.groupby('genre').star_rating.mean())
# Türüne göre ortalamalrı tek tek verir