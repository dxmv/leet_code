# 746. Min Cost Climbing Stairs

class Solution:
    # Time: O(n), Memory: O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        dp[len(cost)]=0
        dp[len(cost)-1]=cost[len(cost)-1]
        for i in range(len(cost)-2,-1,-1):
            dp[i]=min(dp[i+1],dp[i+2])+cost[i]
        return min(dp[0],dp[1])