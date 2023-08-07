# 125. Valid Palindrome
class Solution:
  # Time: O(n), Memory: O(1)
  def isPalindrome(self, s: str) -> bool:
    cs = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    if s=="":
        return True
    l,r=0,len(cs)-1
    while l<=r:
        if cs[l]!=cs[r]:
            return False
        l+=1
        r-=1
    return True