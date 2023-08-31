# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        m=-1
        while l<=r:
            s=min(height[l],height[r])*(r-l)
            if s>m:
                m=s
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return m