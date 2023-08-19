# 128. Longest Consecutive Sequence

class Solution:
    # Time: O(n), Memory: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        mp={}
        for n in nums:
            if n not in mp:
               mp[n]=True
        ma,mi=0,0
        for n in nums:
            current_max,current_min=n,n
            if n in range(mi,ma):
                continue
            while current_min-1 in mp:
                current_min-=1
            while current_max+1 in mp:
                current_max+=1
            if ma-mi<current_max-current_min:
                ma=current_max
                mi=current_min
        return ma-mi+1