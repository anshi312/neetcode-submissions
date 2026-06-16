class Solution:
    def solve(self, board: List[List[str]]) -> None:
#         rows, cols = len(board), len(board[0])

#         def dfs(r, c):
#             # stop if out of bounds or not O
#             if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
#                 return
#             board[r][c] = '#'     # mark safe
#             # explore all 4 directions
#             dfs(r+1, c)
#             dfs(r-1, c)
#             dfs(r, c+1)
#             dfs(r, c-1)

#         # 1. Mark all border-connected O’s as safe
#         for r in range(rows):
#             if board[r][0] == 'O': dfs(r, 0)
#             if board[r][cols-1] == 'O': dfs(r, cols-1)

#         for c in range(cols):
#             if board[0][c] == 'O': dfs(0, c)
#             if board[rows-1][c] == 'O': dfs(rows-1, c)

#         # 2. Flip remaining O’s → X, and # → O
#         for r in range(rows):
#             for c in range(cols):
#                 if board[r][c] == 'O':
#                     board[r][c] = 'X'    # surrounded
#                 elif board[r][c] == '#':
#                     board[r][c] = 'O'    # safe

# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
        # """
        # Do not return anything, modify board in-place instead.
        # """
        rows = len(board)
        cols = len(board[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "#"
            for dr, dc in directions:
                dfs(r + dr, c + dc)


        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] =='O':
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

                elif board[r][c] == "#":
                    board[r][c] = "O"
        