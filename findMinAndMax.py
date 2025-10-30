def findMinAndMax(L):
    if L==[]:
        return (None,None)
    max=min=L[0]
    for i in L:
            if max<= i:
                max=i
            if min>=i:
                min=i
    return (min,max)   
