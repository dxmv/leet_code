# 739. Daily Temperatures


class Solution:
    # Time: O(n), Memory: O(n)
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stack=[]
        ans=[]
        for i in range(len(nums)):
            print(i)
            n=[nums[i]]
            while len(stack)>=1 and n>stack[-1][0] :
                ans[stack[-1][1]]=i-stack[-1][1]
                stack.pop()
            stack.append((n,i))
            ans.append(0)
        return ans
