"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def isUniform(row, col, length):
            value = grid[row][col]
            for r in range(row, row + length):
                for c in range(col, col + length):
                    if grid[r][c] != value:
                        return False
            return True
            
        n = len(grid)

        def build(row, col, size):

            if isUniform(row, col, size):
                return Node(grid[row][col], True, None, None, None, None)
            
            half = size // 2

            return Node(
                1,
                False,
                build(row, col, half),
                build(row, col + half, half),
                build(row + half, col, half),
                build(row + half, col + half, half)
            )

        return build(0, 0, n)