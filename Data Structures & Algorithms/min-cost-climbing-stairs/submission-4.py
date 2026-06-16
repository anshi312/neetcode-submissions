class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp0 = cost[0]
        # dp1 = cost[1]
        # for i in range(len(cost)):
        #     if i < 2:
        #         continue
        #     new_cost = cost[i] + min(dp0, dp1)
        #     dp0 = dp1
        #     dp1 = new_cost
        # return min(dp0, dp1)


        dp = [cost[0], cost[1]]
        for i in range(len(cost)):
            if i < 2:
                continue
            new_cost = cost[i] + min(dp[0], dp[1])
            dp[0] = dp[1]
            dp[1] = new_cost

        return min(dp)