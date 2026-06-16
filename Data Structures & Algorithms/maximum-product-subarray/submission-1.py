class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_here = nums[0]
        min_here = nums[0]
        result = nums[0]

        for n in nums[1:]:
            tmp = max_here
            max_here = max(n, max_here*n, min_here*n)
            min_here = min(n, n*tmp, n*min_here)
            result = max(result, max_here)
        return result   