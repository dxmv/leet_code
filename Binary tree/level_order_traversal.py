# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        ans=[[]]
        level=[]
        q.append(root)
        i=0
        if not root:
            return []
        while len(q)>0:
            current=q.pop(0)
            ans[i].append(current.val)
            if current.left:
                level.append(current.left)
            if current.right:
                level.append(current.right)
            if len(q)==0:
                for n in level:
                    q.append(n)
                i+=1
                level=[]
                if len(q)!=0:
                    ans.append([])
        return ans