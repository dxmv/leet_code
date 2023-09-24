# 70. Climbing Stairs

class Solution:
    # Time: O(n), Memory: O(n)
    def climbStairs(self, n: int) -> int:
        dict={}
        dict[1]=1
        dict[2]=2
        for i in range(3,n+1):
            dict[i]=dict[i-1]+dict[i-2]
        return dict[n]