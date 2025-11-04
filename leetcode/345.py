class Solution:
    def reverseVowels(self, s: str) -> str:
        L=[]
        M=[]
        for i in range(len(s)):
            if s[i] in {'a','e','i','o','u','A','E','I','O','U'}:
                L.append(s[i])
                M.append(i)
        k=0
        s=list(s) #str 是不可变对象
        for j in M[::-1]:
            s[j]=L[k]
            k+=1
        return ''.join(s)
