# 167. Two Sum II - Input Array Is Sorted

class Solution:
  # Time: O(n), Memory: O(1)
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
      left,right=0,len(numbers)-1
      while numbers[left]+numbers[right]!=target and left<=right:
          s=numbers[left]+numbers[right]
          if s<target:
              left+=1
          if s>target:
              right-=1
      return [left+1,right+1]