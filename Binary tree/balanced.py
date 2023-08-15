# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_bal=self.isBalanced(root.left)
        right_bal=self.isBalanced(root.right)
        if not left_bal or not right_bal:
            return False
        left=self.getHeight(root.left)+1
        right=self.getHeight(root.right)+1
        return right==left or right-1==left or right+1==left

    def getHeight(self,root:Optional[TreeNode])->int:
        if not root:
            return 0
        left=self.getHeight(root.left)+1
        right=self.getHeight(root.right)+1
        return max(left,right)
        