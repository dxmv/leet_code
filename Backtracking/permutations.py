# 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def get_perm(nums: List[int],start:int,current:List[int]):
            if len(current)==len(nums):
                if current not in res:
                    res.append(current[:])
                return
            for n in nums:
                if n not in current:
                    current.append(n)
                    get_perm(nums,0,current)
                    current.pop()
        res=[]
        get_perm(nums,0,[])
        return res