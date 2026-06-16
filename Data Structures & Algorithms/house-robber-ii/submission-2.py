class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            if len(arr) == 1:
                return arr[0]

            dp0 = arr[0]
            dp1 = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                value = max(dp1, arr[i]+dp0)
                dp0 = dp1
                dp1 = value
            return dp1

        case1 = rob_linear(nums[1:])
        case2 = rob_linear(nums[:-1])

        return max(case1, case2)