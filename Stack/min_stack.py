# 155. Min Stack

class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_array=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_array) == 0:
            self.min_array.append((0,val))
        elif val<self.min_array[-1][1]:
            self.min_array.append((len(self.stack)-1,val))

    def pop(self) -> None:
        if self.min_array[-1][0]==len(self.stack)-1:
            self.min_array.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_array[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()