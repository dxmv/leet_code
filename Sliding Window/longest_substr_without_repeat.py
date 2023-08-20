# 3. Longest Substring Without Repeating Characters

class Solution:
    # Time: O(n), Memory: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=0
        elements=set()
        m=0
        while r<len(s):
            if s[r] not in elements:
                elements.add(s[r])
                m=max(len(elements),m)
                r+=1
            else:
                elements.remove(s[l])
                l += 1
        return m