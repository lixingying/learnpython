class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from math import gcd
        i=0
        L=""
        while i <=len(str1)-1:
            L=L+str1[i]
            a=len(str1)//len(L)
            if str1!=a*L:
                i=i+1
            else:
                break
        
        b=len(str2)//len(L)
        if str2!=b*L:
            return ""
        else:
            return gcd(a,b)*L    
