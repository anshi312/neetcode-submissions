class Solution:
    def longestPalindrome(self, s: str) -> str:
        # def expand(l, r):
        #     while l>=0 and r<len(s) and s[l]==s[r]:
        #         l -= 1
        #         r += 1
        #     return l+1, r-1
        
        # start, end = 0, 0

        # for i in range(len(s)):
        #     l1, r1 = expand(i, i)
        #     l2, r2= expand(i, i+1)
            
        #     if r1 - l1 > end - start:
        #         start, end = l1, r1
        #     if r2 - l2 > end - start:
        #         start, end = l2, r2

        # return s[start:end+1]

        ##################################################

        # dp[i][j] = True  if s[i:j+1] is a palindrome

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length <= 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and length > max_len:
                    start = i
                    max_len = length

        return s[start : start + max_len]
