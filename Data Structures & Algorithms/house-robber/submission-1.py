class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        dp0 = nums[0]
        dp1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            value = max(dp1, nums[i]+dp0)
            dp0 = dp1
            dp1 = value
        return dp1