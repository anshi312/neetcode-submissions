class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        prev_row = [0] * cols

        for i in range(rows - 1, -1, -1):
            curr_row = [1] * cols
            curr_row[-1] = 1
            for c in range(cols - 2, -1, -1):
                curr_row[c] = prev_row[c] + curr_row[c+1]
            prev_row = curr_row
        return prev_row[0]