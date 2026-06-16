class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max_here = nums[0]
        # min_here = nums[0]
        # result = nums[0]

        # for n in nums[1:]:
        #     tmp = max_here
        #     max_here = max(n, max_here*n, min_here*n)
        #     min_here = min(n, n*tmp, n*min_here)
        #     result = max(result, max_here)
        # return result   

        n, res = len(nums), nums[0]
        prefix = suffix = 0

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        return res
