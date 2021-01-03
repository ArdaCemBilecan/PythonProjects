import pandas as pd

films = pd.read_csv("imdb_1000.csv")
print("ESKİ FİLMS")
print(films.columns)

print(films.drop("content_rating",axis=1).head())  # axis 1 kolon ama axis 1 satır demek
# content rating kolonunu uçur demek bana bunu gösterme demek
# ana filmsten silmaz sadece bu halini basar başka bir değişkene at

films = films.drop("content_rating",axis=1)
print("YENİ FİLMS")
print(films.columns)


print("SATIR SİLME")

films = films.drop(1,axis=0) # 1.(index) satırı sil

print(films.head())

rowsToDrop=[0,2,3,4,5,6,7] # Bu indextekiler silinsin demek

films=films.drop(rowsToDrop,axis=0)

print(films)