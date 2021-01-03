import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns=["İsim","Soyisim","SSN","Test1","Test2","Test3","Test4","Final","Sonuc"]

print(notlar)
print("------------------------------------")
print(notlar.loc[:,"İsim"]) # İsim kolonnu ver demek
print("------------------------------------")
print(notlar.loc[:5,"İsim"]) #isimlerden index 5'e kadar (dahil) göster demek. 6 Kayıt göreceksin
print("------------------------------------")

print(notlar.loc[:5,"İsim":"Test3"])  # ilk 6 kaydın test3 dahil oraya kadar görmek istiyorum
print("------------------------------------")
print(notlar.loc[:5,["İsim","Soyisim","Final"]])  # bana sadece final, soyiim,isim ver demek

print("------------------------------------")

print(notlar.loc[::-1,"İsim"]) #☺ tersten bastırır