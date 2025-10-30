def createCounter():
    i=0
    def counter():
        nonlocal i
        i=i+1
        return i
    return counter
