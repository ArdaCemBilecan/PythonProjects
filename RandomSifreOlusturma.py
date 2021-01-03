# Kullanıcıya Random Şifre atama
import string
import random

buyukHarf=[]  # rand 0
kucukHarf=[] # rand 1
rakamlar=[]  # rand 2
ozelKarakter=["_",":","/","*","-","<",">"] #rand 3
sifre=""
kucukHarf=(string.ascii_lowercase)
buyukHarf=(string.ascii_uppercase)
for i in range(10):
    rakamlar.append(str(i))


karakterSayisi = int(input("Kaç haneli bir şifre istiyorsunuz? : "))
while karakterSayisi <=6 :
    print("En az 7 Karakter olmalı!")
    karakterSayisi = int(input("Kaç haneli bir şifre istiyorsunuz? : "))

for i in range(karakterSayisi):
    rand = random.randint(0,3)
    if rand == 0:
        x = random.randint(0,len(buyukHarf)-1)
        sifre = sifre+buyukHarf[x]
    elif rand == 1:
        x = random.randint(0,len(kucukHarf)-1)
        sifre = sifre+kucukHarf[x]
    elif rand ==2:
        x = random.randint(0,9)
        sifre = sifre+rakamlar[x]
    else:
        x=random.randint(0,len(ozelKarakter)-1)
        sifre=sifre+ozelKarakter[x]

print(sifre)
        
    

    

