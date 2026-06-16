# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def valid(node, left, right):
        #     if not node: return True
        #     if not (left < node.val < right): return False
        #     return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        # return valid(root, float('-inf'), float('inf'))

        self.prev = float('-inf')

        def inorder(node):
            if not node:
                return True

            if not inorder(node.left):
                return False

            if node.val <= self.prev:
                return False
            self.prev = node.val

            return inorder(node.right)

        return inorder(root)