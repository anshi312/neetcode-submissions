# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def maxLength(root):
            if not root: return 0
            nonlocal diameter
            left = maxLength(root.left)
            right = maxLength(root.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        maxLength(root)
        return diameter