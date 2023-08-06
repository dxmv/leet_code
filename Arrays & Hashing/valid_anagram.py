# 242. Valid Anagram
class Solution:
    # Time: O(n) Memory: O(n)   
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map={}
        for n in s:
            if n in map:
                map[n]+=1
            else:
                map[n]=1
        for n in t:
            if n in map:
                map[n]-=1
            else:
                return False

    # Time: O(n*logn) Memory: O(1)        
    def isAnagram(self, s: str, t: str) -> bool:
      return sorted(s)==sorted(t)