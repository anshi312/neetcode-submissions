class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, curr_sum):
            if curr_sum == amount:
                return 1

            if curr_sum > amount or i >= len(coins):
                return 0

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            take = dfs(i, curr_sum + coins[i])
            take_next = dfs(i + 1, curr_sum)
            ways = take + take_next

            memo[(i, curr_sum)] = ways

            return ways

        return dfs(0, 0)            