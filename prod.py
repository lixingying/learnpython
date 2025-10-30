from functools import reduce
def f(x,y):
        return x*y    
def prod(L):
        return reduce(f,L)
        
