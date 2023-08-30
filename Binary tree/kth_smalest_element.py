# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Time: O(n), Memory: O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root:Optional[TreeNode],arr):
            if not root:
                return
            dfs(root.left,arr)
            arr.append(root.val)
            dfs(root.right,arr)
        arr=[]
        dfs(root,arr)
        return arr[k-1]