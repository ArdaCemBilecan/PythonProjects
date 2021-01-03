def f(x,y):
    return (-y/x)

def f1(x):
    return (-2*x**3 + 12*x**2 - 20*x + 8.5)

# Euler Yaklaştırma Methodu

x0 = 4
x1 = 7
y0 = 0.75
h = 0.0001

while(x0 < x1 ):
    y0+=f(x0,y0)*h
    x0+=h
print(y0)
    

# İyileştirilmiş Euler Methodu

x0 = 4
x1 = 7
y0 = 0.75
h = 1
print("****************")
while(x0 < x1 ):
    y12=y0+f(x0,y0)*h/2
    x0+=h/2
    y0=y0+f(x0,y12)*h
    x0+=h/2
    print(y12 , y0)

# Heun Methodu
    
x0 = 4
x1 = 7
y0 = 0.75
h = 1
print("****************")
while(x0 < x1 ):
    y0p = y0+f(x0,y0)*h
    y0 = y0+( f(x0,y0) + f(x0+h,y0p) )*h/2
    x0+=h
    print(y0 , y0p)

# Soru Çözümü: 

x0 = 0
x1 = 4
y0 =-2
h=1

while (x0<x1):
    y0p = y0+f1(x0)*h
    y0 =y0+(f1(x0)+f1(x0+h))*h/2
    x0+=h
    print(y0)
    



    

