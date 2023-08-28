# 33. Search in Rotated Sorted Array

class Solution:
    # Time: O(logn), Memory: O(1)
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        if nums[l]<=nums[r]:
            return self.bs(l,r,target,nums)   
        pivot=-1     
        while l<r:
            mid=(l+r)//2
            current=nums[mid]
            if mid>0 and current<nums[mid-1]:
                pivot=mid
            if current>nums[r]:
                l=mid+1
            elif current<nums[r]:
                r=mid-1
        if pivot==-1:
            pivot=l if nums[l]<=nums[r] else r
        if target>=nums[0] and target<=nums[pivot-1]:
            return self.bs(0,pivot,target,nums)
        if target>=nums[pivot] and target<=nums[-1]:
            return self.bs(pivot,len(nums)-1,target,nums)
        return -1

    def bs(self,l,r,target,nums):
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        while l<=r:
            mid=(l+r)//2
            current=nums[mid]
            if current==target:
                return mid
            if current>target:
                r=mid-1
            else:
                l=mid+1
        return -1