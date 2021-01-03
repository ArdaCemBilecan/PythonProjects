# Newton Raphson metodu ile karekök bulma
while(True):
    sayi = float(input("Hangi Sayının Karekökü Hesaplanacak: "))
    x = sayi
    if sayi ==-1:
        break
    hassasiyet = 10**(-10)
    while abs(sayi-x*x)>hassasiyet:
        x = (x+sayi/x)/2
    print(x)
    

print("HOCANIN KODU İSE AŞAĞIDADIR")
    
#def f(x):
#    return (x**2-a)
#
#def fi(x):
#    return 2*x
#
#
#x2,t = 0,1
#
#def hata(x1,x2):
#    return (x1-x2)/x1
#
#
#x1 = int(input("Başlangıç Değerini Giriniz: "))
#a= int(input("Hangi Sayının Karekökü Hesaplanacak: "))
#
#if a>0:
#    while (abs(hata(t,x2))>0.0001):
#        x2 = x1-f(x1)/fi(x1)
#        print(hata(x1,x2),x1,x2)
#        t = x1
#        x1 = x2
#else:
#    print("Sayı 0 dan büyük olmalı")
        
