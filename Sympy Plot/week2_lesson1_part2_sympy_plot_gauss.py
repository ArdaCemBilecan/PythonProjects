import sympy as sym
import sympy.plotting as syp
import matplotlib.pyplot as plt

sym.init_printing()  # display methodunu pprint haline çevirir
#pprint fonksiyonunna göre daha güzel bir çıktı veriyor o yüzden bunu seçtim

sigma = sym.Symbol('sigma') # hangi matematiksel sembole eşit gelidğini söyledik
mu = sym.Symbol('mu')
x=sym.Symbol('x')
sym.pprint(2*sym.pi*sigma)  # pprint fonksiyonu özel isimli değişkenleri sembollü halini verir.
# pi , sigma , alfa , beta gibi
#display(1/(sym.sqrt(2*sym.pi*sigma**2)))

part1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
#display(part1)

part2=sym.exp(-1*((x-mu)**2)/(2*sigma**2))

#display(part2)

gauss_function = part1*part2
gauss_function.subs({mu:0,sigma:1})
display(gauss_function)  
#sym.pprint(gauss_function)
# Bunun grafiğini çizmek istersek o zaman:
syp.plot(gauss_function.subs({mu:1,sigma:3}),(x,-10,10),title='Gauss')
# .plot grafiğini çizdirir. 3 Paremetre verdik. !. parametre için mu ve sigma için
# hangi değerler olacağını belirledik. 2. parametrede x in hangi değer aralıklarında
#değer alacağını belirledik. 3. de ise bir isim verdik


# bu işlemi for döngüsü ile yapalım
x_values=[]
y_values=[]
for value in range(-10,10):
    y = gauss_function.subs({mu:1,sigma:3,x:value}).evalf()
    #evalf ise gauss_function.subs({mu:1,sigma:3,x:value}) matematiksel hale dönüştürür.
    x_values.append(value)
    y_values.append(y)

plt.plot(x_values,y_values) # grafikte x değerleri için hangi y değerlerine karşılık geldiğini atıyoruz
plt.show()  # grafiği console da gösteriyoruz
# syp.plot(gauss_function.subs({mu:1,sigma:3}),(x,-10,10),title='Gauss')
# bu işlemi for döngüsü ve matplotlib kütüphanesi ile yaptırıyoruz


