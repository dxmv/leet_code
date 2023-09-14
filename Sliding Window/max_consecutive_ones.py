# These are not in the list
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

# 487. Max Consecutive Ones II
class Solution:

    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        l,r=0,0
        current=0
        res=0
        index_zero=-1
        while r<=len(nums)-1:
            c=nums[r]
            if c==1:
                current+=1
            else:
                if index_zero==l:
                    l+=1
                    current-=1
                if index_zero!=-1:
                    nums[index_zero]=0
                index_zero=r
                nums[index_zero]=1
                current+=1
            res=max(current,res)
            r+=1
        return res

# 1004. Max Consecutive Ones III
