# 1. Two Sum
class Solution:
  # Time: O(n), Memory: O(n)
  def twoSum(self, nums: List[int], target: int) -> List[int]:
      map={}
      for i in range(0,len(nums)):
          if nums[i] in map:
              arr=[map[nums[i]]]
              arr.append(i)
              map[nums[i]]=arr
          else:
              map[nums[i]]=i
      for n in nums:
          if target-n in map and map[target-n]!=map[n]:
              return [map[n],map[target-n]]
          elif target-n==n and not isinstance(map[n], int):
              return [map[n][0],map[n][1]]
      return [0,0]
  # Time: O(n^2), Memory: O(1)
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(0,len(nums)):
        current=nums[i]
        for j in range(0,len(nums)):
            if i==j:
                continue
            elif current+nums[j]==target:
                return [i,j]
    return [0,0]
