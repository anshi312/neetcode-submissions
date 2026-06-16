class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #------ add memo -------#

        memo = {}

        def dfs(row, col):
            if row == m - 1 or col == n - 1:
                return 1

            if row >= m or col >= n:
                return 0

            if (row, col) in memo:
                return memo[(row, col)]

            memo[(row, col)] = dfs(row + 1, col) + dfs(row, col + 1)
            return memo[(row, col)]

        return dfs(0, 0)


        #------brute force-------#

        # def dfs(row, col):
        #     if row == m - 1 or col == n - 1:
        #         return 1

        #     paths = 0

        #     if col + 1 < n:
        #         paths += dfs(row, col + 1)

        #     if row + 1 < m:
        #         paths += dfs(row + 1, col)

        #     return paths

        # return dfs(0, 0)



        #################################

        # rows = m
        # cols = n
        # prev_row = [0] * cols

        # for i in range(rows - 1, -1, -1):
        #     curr_row = [1] * cols
        #     curr_row[-1] = 1
        #     for c in range(cols - 2, -1, -1):
        #         curr_row[c] = prev_row[c] + curr_row[c+1]
        #     prev_row = curr_row
        # return prev_row[0]

        