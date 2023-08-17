class Solution:
  # Time: O(n), Memory: O(n)
  def productExceptSelf(self, nums: List[int]) -> List[int]:
      left=1
      answer=[]
      for n in nums:
          answer.append(left)
          left*=n
      right=1
      for i in range(len(nums)-1,-1,-1):
          answer[i]*=right
          right*=nums[i]
      return answer