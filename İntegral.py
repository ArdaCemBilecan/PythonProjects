from math import e
def f(x):
    return (e**x)


a=0
b=3
deltax = 0.0001
# Burada integrali idkdörtgen alanı ile hesaplamaya çalışıyor
n = int((b-a)/deltax)
integral = 0
for i in range(n):
    integral+= f(a)*deltax
    a+=deltax

print(integral)



# Burda da ortalama değerler alarak gidiyoruz. Bir önceki kadar
#deltaxi küçültmemize gerek kalmıyor 
integral = 0
a=0
b=3
deltax=0.01
n = int((b-a)/deltax)
for i in range(n):
    integral+=deltax*(f(a)+f(a+deltax))/2
    a+=deltax

print("Ortalama İntegral: ",integral)