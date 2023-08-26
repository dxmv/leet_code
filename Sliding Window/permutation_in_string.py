# 567. Permutation in String

class Solution:
    # Time: O(n^2), Memory: O(n)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp={}
        for s in s1:
            if s in mp:
                mp[s]+=1
            else:
                mp[s]=1
        l=r=0
        for r in range(len(s2)):
            if s2[r] in mp:
                if mp[s2[r]]-1<0:
                    while s2[l] != s2[r]:
                        mp[s2[l]] += 1
                        l += 1
                    l += 1
                    continue
                mp[s2[r]]-=1
                all=True
                for k,v in mp.items():
                    if v!=0:
                        all=False
                if all:
                    return True
                r+=1
            else:
                while l < r:
                    mp[s2[l]] += 1
                    l += 1
                r+=1
                l=r
        return False