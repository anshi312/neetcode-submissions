class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        row_zeros = set()
        col_zeros = set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row_zeros.add(row)
                    col_zeros.add(col)
        
        for row in row_zeros:
            for col in range(cols):
                matrix[row][col] = 0
        
        for col in col_zeros:
            for row in range(rows):
                matrix[row][col] = 0
                
        