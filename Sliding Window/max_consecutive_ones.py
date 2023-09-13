# 485. Max Consecutive Ones

class Solution:
    # Time: O(n), Memory: O(1)
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num_ones=0
        current=0
        l,r=0,0
        while r<=len(nums)-1:
            if nums[r]==1:
                current+=1
            else:
                num_ones=max(num_ones,current)
                current=0
                l=r
            r+=1
        return max(num_ones,current)

# 1004. Max Consecutive Ones III
