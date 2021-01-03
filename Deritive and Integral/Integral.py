import sympy as sp
x = sp.Symbol('x')
p = sp.exp(-(x-10)**2/2)/sp.sqrt(2*sp.pi)
display(p)
result = sp.Integral(p,(x,11,12)).doit().evalf()
display(result)


# GİTHUB   https://github.com/ArdaCemBilecan/Programlama-Lab