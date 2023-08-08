# 20. Valid Parentheses
class Solution:
    # Time: O(n), Memory: O(n)
    def isValid(self, s: str) -> bool:
        stack=[]
        map={"{":"}","[":"]","(":")"}
        for v in s:
            if v in "({[":
                stack.append(v)
            else:
                if len(stack)==0:
                    return False
                last=stack.pop()
                if map[last]!=v:
                    return False
        return len(stack)==0