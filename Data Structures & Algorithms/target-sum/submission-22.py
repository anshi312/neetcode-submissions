class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #----------knapsack---------------------------------#

        total = sum(nums)

        if abs(target) > total or (total + target) % 2 != 0:
            return 0

        subset_sum = (total + target) // 2

        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] = dp[j] + dp[j - num]

        return dp[subset_sum]


        #--------- recursion + memo -------------------------#
        memo = {}

        def dfs(i, curr_sum):
            if i == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0
            
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            add_curr = dfs(i + 1, curr_sum + nums[i])
            sub_curr = dfs(i + 1, curr_sum - nums[i])

            ways = add_curr + sub_curr
            memo[(i, curr_sum)] = ways

            return ways

        return dfs(0, 0)



        #######################################################
        #######################################################

        # dp = [defaultdict(int) for _ in range(len(nums)+1)]

        # dp[0][0] = 1

        # for i in range(len(nums)):
        #     for curr_sum, count in dp[i].items():
        #         dp[i+1][curr_sum + nums[i]] += count
        #         dp[i+1][curr_sum - nums[i]] += count
        # return dp[len(nums)][target]


        # # dp = {}
        # # def backtrack(i, curr_sum):
        # #     if i == len(nums):
        # #         return 1 if curr_sum == target else 0

        # #     if (i, curr_sum) in dp:
        # #         return dp[(i, curr_sum)]

        # #     positive = backtrack(i + 1, curr_sum + nums[i])
        # #     negative = backtrack(i + 1, curr_sum - nums[i])
            
        # #     dp[(i, curr_sum)] = positive + negative
        # #     return dp[(i, curr_sum)]

        # # return backtrack(0, 0)