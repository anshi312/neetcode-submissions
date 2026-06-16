class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            curr_val = matrix[row][col]
            max_length = 1

            for dr, dc in directions:
                nxt_row = dr + row
                nxt_col = dc + col

                if (0 <= nxt_row < rows and 0 <= nxt_col < cols and matrix[nxt_row][nxt_col] > curr_val):
                    length = 1 + dfs(nxt_row, nxt_col)
                    max_length = max(length, max_length)

            return max_length

        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))

        return ans


