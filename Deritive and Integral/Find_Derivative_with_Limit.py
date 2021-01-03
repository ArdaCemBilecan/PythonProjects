from sympy import Symbol,Limit
t =Symbol('t')
t1 = Symbol('t1')
delta_t=Symbol('delta_t')
St = 5*t**2 + 2*t + 8
St1 = St.subs({t:t1})
#st1 = 5*(t1**2)+2*t1+8
St1_delta=St.subs({t:t1+delta_t})
display(St1_delta)
#St1_delta = 5*(t1+delta_t)**2 + (t1+delta_t)*2+8
display(((5*(t1+delta_t)**2 + (t1+delta_t)*2+8) - 5*(t1**2)+2*t1+8 ) / delta_t)
result=Limit((St1_delta-St1)/delta_t,delta_t,0).doit()
display(result)

# GİTHUB   https://github.com/ArdaCemBilecan/Programlama-Lab