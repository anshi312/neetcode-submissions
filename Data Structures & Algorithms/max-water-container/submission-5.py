class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0

        left = 0
        right = len(heights) - 1
        while left < right:
            curr_volume = (right - left) * min(heights[left], heights[right])
            volume = max(volume, curr_volume)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return volume


        