import sympy as sp

sp.init_printing()

x = sp.Symbol('x')
y,z = sp.symbols('y,z')
f = sp.Function('f')
g = x**2+y**2+z**2
display(g)     # sp.pprint(g) --> Bize çıktıyı sembolleştirirler

# Kucuk bir örnek: x**2 +2x-5 i yazdıralım

h = x**2 +2*x -5
display(h)

# h.subs(x,2) dersem x yerine 2 yazar ve bize sonucu verir
# h.subs(x,z) dersem x yerine z yazar ve bize z türünden sonucu verir

print("H Fonksiyoun sonucu: "+str(h.subs(x,1.5)))
display(h.subs(x,z))


#sp.simplify(h) idafeyi sadeleştirir.
h = (x**2-x-6)/(x**2-3*x)
#print(h.simplify(1)) tercihi kullanım aşağıda
print(sp.simplify(h))

# Verilen Çarpmım ifadesini açar  sp.expand(f)
f= (x+1)**3 * (x-2)**2
display(sp.expand(f))

# sp.factor(f)  Dağıtılmış şeklinde verilen ifadeyi çarpanlara ayırır.
f = 3*x**4 - 36*x**3 + 99*x**2 - 6*x -144
display(f)
display("ÇARPANLARA AYRILMIŞ HALİ: ",sp.factor(f))

# Örnek: x + x**2/2 + x**3/3 + x**4/4 + .... x**n/n
x = sp.Symbol('x')
# simdilik n = 10 olsun
n = 10
series = x
for i in range (2,n+1):
    series = series + (x**i)/i
display(series)
sonuc = float(series.subs(x,2))
print(sonuc)


# Birden fazla değişkene değer atama işlemi:
expr = x*x+x*y+y*x+y*y
res = expr.subs({x:1,y:2})
print(res)

# expr de x yerine 1-y yazdırırsak:
res = expr.subs(x,1-y)
display(res)






    