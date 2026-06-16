class Solution:
    def totalNQueens(self, n: int) -> int:
        result = []
        board = ['.' * n for _ in range(n)]

        cols = set()
        left_diag = set()
        right_diag = set()

        def backtrack(r):
            if r == n:
                result.append(board.copy())
                return

            for c in range(n):
                if c in cols or (r-c) in left_diag or (r+c) in right_diag:
                    continue
                
                board[r] = board[r][:c] + "Q" + board[r][c+1:]
                cols.add(c)
                left_diag.add(r-c)
                right_diag.add(r+c)

                backtrack(r+1)

                board[r] = board[r][:c] + "." + board[r][c+1:]
                cols.remove(c)
                left_diag.remove(r-c)
                right_diag.remove(r+c)
        
        backtrack(0)
        return len(result)   