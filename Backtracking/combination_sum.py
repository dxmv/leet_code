# 39. Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start:int, target:int, current:List[int]):
            if target < 0:
                return
            if target == 0:
                res.append(current.copy())
                return
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, target - candidates[i], current)
                current.pop()
        
        res = []
        backtrack(0, target, [])
        return res