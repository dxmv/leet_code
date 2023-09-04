# 875. Koko Eating Bananas

class Solution:
    # Time:O(nlogn), Memory: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        while left<right:
            k=(left+right)//2
            if self.eat(piles,h,k):
                right=k
            else:
                left=k+1
        return right
    
    def eat(self,piles:List[int],hours:int,k:int)->True:
        for i in range(len(piles)):
            if hours<0:
                return False
            current=piles[i]
            hours-=(current//k)
            if current%k!=0:
                hours-=1
        if hours<0:
            return False
        return True