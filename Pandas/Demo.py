import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns=["İsim","Soyisim","SSN","Test1","Test2","Test3","Test4","Final","Sonuc"] #şeklinde kendin ayarlayabilirsin
print(notlar)
print("----------------")
print(notlar["Soyisim"])
print("----------------")
#print(notlar.head())
#print(notlar.tail())
filtre = notlar["Soyisim"] =="Alfalfa"
print(notlar[filtre])

print("----------------")

print(notlar["Final"])
