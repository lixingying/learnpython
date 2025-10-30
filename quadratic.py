import math

def quadratic(a,b,c):
    delta=math.sqrt(b**2-4*a*c)
    r_1=(-b+delta)/(2*a)
    r_2=(-b-delta)/(2*a)
    return r_1, r_2
