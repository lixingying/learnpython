class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        i=0
        TF=[]
        while i<len(candies):
            if max(candies)<=candies[i]+extraCandies:
                TF.append(True)
            else:
                TF.append(False)
            i+=1
        return TF
