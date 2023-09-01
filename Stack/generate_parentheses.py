# 22. Generate Parentheses

class Solution:
    # Time: O(n!*n), Memory: O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        arr=set()
        self.generate("","(",n,n*2,arr)
        return arr
        
    def generate(self,current:str,add:str,n:int,len_str:int,arr)->None:
        if len(current)==len_str:
            if self.isValid(current):
                arr.add(current)
            return
        current+=add
        self.generate(current,"(",n,len_str,arr)
        self.generate(current,")",n,len_str,arr)


    def isValid(self, s: str) -> bool:
        stack=[]
        for v in s:
            if v == "(":
                stack.append(v)
            else:
                if len(stack)==0:
                    return False
                last=stack.pop()
        return len(stack)==0