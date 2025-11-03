class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        A=0
        while i<len(flowerbed) and flowerbed[i]==0:
            A+=1
            i+=1
        L=[]
        while i<len(flowerbed):
            if flowerbed[i]==1:
                i+=1
            else:
                L.append(0)
                while i<len(flowerbed) and flowerbed[i]==0:
                    L[len(L)-1]+=1
                    i+=1
        if flowerbed[len(flowerbed)-1]==1:
            C=0
            B=L
        else:
            if len(L)>0:
                C=L[len(L)-1]
                B=L[0:len(L)-1]
            else:
                return (A+1)//2>=n
        m=0
        for i in range(len(B)):
            m=m+((L[i]-1)//2)
        return (A//2)+(C//2)+m>=n
                
