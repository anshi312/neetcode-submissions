class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n < 3:
            if n == 0:
                return 0
            else:
                return 1

        for i in range(n + 1):
            if i < 3:
                continue
            t3 = sum(dp)
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = t3

        return dp[2]