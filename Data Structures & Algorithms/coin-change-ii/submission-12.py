class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #-----------we have to find sum, so kinda knapsack------#

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = dp[j] + dp[j - coin]

        return dp[amount]       



        #----------- yes i did this on my own-------------#
        # memo = {}

        # def dfs(i, curr_sum):
        #     if curr_sum == amount:
        #         return 1

        #     if curr_sum > amount or i >= len(coins):
        #         return 0

        #     if (i, curr_sum) in memo:
        #         return memo[(i, curr_sum)]

        #     take = dfs(i, curr_sum + coins[i])
        #     take_next = dfs(i + 1, curr_sum)
            
        #     memo[(i, curr_sum)] = take + take_next

        #     return memo[(i, curr_sum)]

        # return dfs(0, 0)            