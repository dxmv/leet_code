# 572. Subtree of Another Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # If s is the number of nodes in root, and t the number of nodes in subRoot, then:
    # Time: O(s*t), Memory: O(1)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(t1,t2):
            if not t1 and not t2:
                return True
            if not t2 or not t1:
                return False
            if t1.val!=t2.val:
                return False 
            return isSameTree(t1.left,t2.left) and isSameTree(t1.right,t2.right)
        isSub=False
        if not root:
            return False
        if root.val==subRoot.val:
            isSub=isSameTree(root,subRoot)
        return isSub or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)  