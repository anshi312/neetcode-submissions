class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        #--------- recursion + memo -------------------------#

        def dfs(i, curr_sum):
            if i == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0

            add_curr = dfs(i + 1, curr_sum + nums[i])
            sub_curr = dfs(i + 1, curr_sum - nums[i])

            ways = add_curr + sub_curr

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