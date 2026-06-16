class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        toprow, bottomrow = 0, len(matrix) - 1
        while toprow <= bottomrow:
            midrow = (toprow+bottomrow)//2
            if matrix[midrow][0] <= target and target <= matrix[midrow][-1]:
                #binary search here
                left, right = 0, len(matrix[0]) - 1
                
                while left <= right:
                    m = (left + right) // 2
                    if matrix[midrow][m] == target:
                        return True
                    elif matrix[midrow][m] < target:
                        left = m + 1
                    else:
                        right = m - 1
                
                return False  # Not found in this row

            elif target < matrix[midrow][0]:
                bottomrow = midrow - 1
            else: 
                toprow = midrow + 1
            
        return False
