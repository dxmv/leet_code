# 543. Diameter of Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Very slow solution
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_d=self.diameterOfBinaryTree(root.left)
        right_d=self.diameterOfBinaryTree(root.right)
        left=self.getHeight(root.left)
        right=self.getHeight(root.right)
        return max(left_d,right_d,left+right)
    def getHeight(self,root:Optional[TreeNode])->int:
        if not root:
            return 0
        left=self.getHeight(root.left)+1
        right=self.getHeight(root.right)+1
        return max(left,right)
    