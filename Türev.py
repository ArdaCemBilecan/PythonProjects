def nCr(n,r):
    from math import factorial
    return(factorial(n)/(factorial(r)*factorial(n-r)))
    # GEnel formu için !
def f(x):
    return(x**3+2*x+8)
    
# ileri sonlu farklar    
x0 = 1
h = 0.001
xprime = (f(x0+h)-f(x0))/h
print("İleri Sonlu Farklar: ",xprime) 

# Geri Sonlu Farklar
x0 = 1
h = 0.001
xprime = (f(x0)-f(x0-h))/h
print("Geri Sonlu Farklar: ",xprime)


# Merkezi Farklar

x0 = 1
h= 0.001

xprime = (f(x0+h) - f(x0-h))/2*h

print("Merkezi Farklar: ",xprime)


# Genel Formu: 
x0 = 1
h = 0.001
n = 3
xprime = 0
for k in range(n+1):
    xprime += (-1)**(k+n)*nCr(n,k)*f(x0+k*h)
    
a = xprime * (1/(h**n))
print("Genel Form: ",a)
    




