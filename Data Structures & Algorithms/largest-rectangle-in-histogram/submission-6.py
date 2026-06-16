class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            left = i        # i = 4 ; h = 2

            while stack and stack[-1][1] > h:
                index, height = stack.pop()          
                max_area = max(max_area, height * (i - index))
                left = index 
            
            stack.append((left, h)) # (0, 1) (2, 2) (4, 2) (5, 4)

        for idx, h in stack:
            area = h * (len(heights) - idx)
            max_area = max(max_area, area)

        return max_area

