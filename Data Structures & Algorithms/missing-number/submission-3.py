class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # given_sum = sum(nums)
        # n = len(nums)
        # ideal_sum = ((n + 1) * n) // 2

        # return ideal_sum - given_sum

        #------ without risk of overflow---------#

        res = len(nums)

        for i in range(len(nums)):
            res ^= i ^ nums[i]

        return res