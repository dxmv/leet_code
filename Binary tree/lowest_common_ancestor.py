# 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        smaller,bigger=min(p.val,q.val),max(p.val,q.val)
        while root:
            if root.val>=smaller and root.val<=bigger:
                return root
            elif root.val>smaller and root.val>bigger:
                root=root.left
            elif root.val<smaller and root.val<bigger:
                root=root.right
        return -1