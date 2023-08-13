# 49. Group Anagrams

class Solution:
    # Time: O(n*logn), Memory: O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        for s in strs:
            ss=''.join(sorted(s))
            print(ss)
            if ss in mp:
                mp[ss].append(s)
            else:
                mp[ss]=[s]
        return [value for value in mp.values()]
        