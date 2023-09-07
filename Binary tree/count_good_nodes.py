# 1448. Count Good Nodes in Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(n), Memory: O(1), n-number of nodes
    def goodNodes(self, root: TreeNode) -> int:
        return self.isGood(root,float('-inf'))
        
    def isGood(self,root:TreeNode,m:int):
        if not root:
            return 0
        end=0
        if root.val>=m:
            m=root.val
            end=1
        l=self.isGood(root.left,m)
        r=self.isGood(root.right,m)
        return l+r+end