# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def getSubsets(nums:List[int],current:List[int],start:int):
            res.append(current.copy())
            if start>=len(nums):
                return
            for i in range(start,len(nums)):
                current.append(nums[i])
                getSubsets(nums,current,i+1)
                current.pop()
        res=[]
        getSubsets(nums,[],0)
        return res
