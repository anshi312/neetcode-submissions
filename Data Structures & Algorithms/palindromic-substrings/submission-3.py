class Solution:
    def countSubstrings(self, s: str) -> int:
        # def expand(l, r):
        #     count = 0
        #     while l>=0 and r<len(s) and s[l]==s[r]:
        #         count += 1
        #         l -= 1
        #         r += 1
        #     return count
        
        # total = 0

        # for i in range(len(s)):
        #     total += expand(i, i)
        #     total += expand(i, i+1)

        # return total

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        count = 0

        for i in range(n):
            dp[i][i] = True
            count += 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                if dp[i][j]:
                    count += 1

        return count