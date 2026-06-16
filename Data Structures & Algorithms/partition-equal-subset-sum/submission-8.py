class Solution:
    def canPartition(self, nums: List[int]) -> bool:

#------ most optimal knapsack dp ------_#
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]


#------ set method for 0/1 knapsack------_#

        # if sum(nums) % 2 != 0:
        #     return False

        # target = sum(nums) // 2

        # totals_possible = set()
        # totals_possible.add(0)

        # for num in nums:
        #     next_set = set()
        #     for total in totals_possible:
        #         next_set.add(total + num)
        #         next_set.add(total)
        #     totals_possible = next_set

        # return True if target in totals_possible else False







#----------------knapsack kinda dp-----------#

        # total = sum(nums)
        # if total % 2 != 0:
        #     return False

        # target = total // 2
        # dp = [False] * (target + 1)
        # dp[0] = True

        # for num in nums:
        #     for s in range(target, num - 1, -1):
        #         if dp[s - num]:
        #             dp[s] = True

        # return dp[target]

#------------- recursion memoized --------------#

        # total = sum(nums)
        # if total % 2 != 0:
        #     return False

        # target = total // 2
        # n = len(nums)

        # memo = {}   

        # def dfs(idx, curr_sum):
        #     if curr_sum == target:
        #         return True

        #     if curr_sum > target or idx >= n:
        #         return False

        #     if (idx, curr_sum) in memo:
        #         return memo[(idx, curr_sum)]

        #     take = dfs(idx + 1, curr_sum + nums[idx])
        #     not_take = dfs(idx + 1, curr_sum)

        #     memo[(idx, curr_sum)] = take or not_take
        #     return take or not_take

        # return dfs(0, 0)