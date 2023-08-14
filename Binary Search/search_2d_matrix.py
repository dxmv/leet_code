# 74. Search a 2D Matrix
class Solution:
    # Time: O(log(n*m)), Memory: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums: List[int], target: int) -> bool:
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                return binary_search(matrix[mid], target)
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        return False
