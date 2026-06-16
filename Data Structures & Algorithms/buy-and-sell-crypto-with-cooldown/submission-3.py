class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)





        # if not prices: return 0

        # hold = -prices[0]
        # sold = 0
        # rest = 0

        # for price in prices[1:]:
        #     prev_hold = hold
        #     prev_sold = sold
        #     prev_rest = rest

        #     hold = max(prev_hold, prev_rest - price)
        #     sold = prev_hold + price
        #     rest = max(prev_rest, prev_sold)    
        # return max(sold, rest)