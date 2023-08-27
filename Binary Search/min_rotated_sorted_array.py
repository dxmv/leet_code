# 153. Find Minimum in Rotated Sorted Array

class Solution:
    # Time: O(logn), Memory: O(1)
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<r:
            print(l,r)
            mid=(l+r)//2
            current=nums[mid]
            if mid>0 and current<nums[mid-1]:
                return current
            if current>nums[r]:
                l=mid+1
            elif current<nums[r]:
                r=mid-1
        return min(nums[l],nums[r])