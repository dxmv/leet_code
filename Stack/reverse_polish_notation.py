# 150. Evaluate Reverse Polish Notation

class Solution:
    # Time: O(n), Memory: O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        operations=set(["+","*","/","-"])
        stack=[]
        for t in tokens:
            if t in operations:
                first=int(stack.pop())
                second=int(stack.pop())
                stack.append(int(self.operation(second,first,t)))
            else:
                stack.append(t)
        return int(stack[0])
        
    def operation(self,x,y,o):
        if o=="+":
            return x+y
        if o=="-":
            return x-y
        if o=="*":
            return x*y
        if o=="/":
            return x/y