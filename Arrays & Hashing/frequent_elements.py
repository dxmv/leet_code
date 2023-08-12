# 347. Top K Frequent Elements
class Solution:
    # Time: O(n*logn), Memory:O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        if k == 0:
            return []
        for n in nums:
            if n in mp:
                mp[n] += 1
            else:
                mp[n] = 1
        arr = []
        for key, value in mp.items():
            arr.append((key, value))
        sorted_data = sorted(arr, key=lambda x: x[1], reverse=True)
        res = []
        if k == 1:
            return [sorted_data[0][0]]
        for i in range(k):
            res.append(sorted_data[i][0])
        return res