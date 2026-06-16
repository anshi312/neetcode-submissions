class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]



        # # rows = len(text1) + 1
        # # cols = len(text2) + 1
        # # dp = [[0] * cols for _ in range(rows)]

        # # for i in range(rows - 2, -1, -1):
        # #     for j in range(cols - 2, -1, -1):
        # #         if text1[i] == text2[j]:
        # #             dp[i][j] = 1 + dp[i+1][j+1]
        # #         else:
        # #             dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        # # return dp[0][0]

        # if len(text1) < len(text2):
        #     text1, text2 = text2, text1

        # prev = [0] * (len(text2) + 1)
        # curr = [0] * (len(text2) + 1)

        # for i in range(len(text1) - 1, -1, -1):
        #     for j in range(len(text2) - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             curr[j] = 1 + prev[j + 1]
        #         else:
        #             curr[j] = max(curr[j + 1], prev[j])
        #     prev, curr = curr, prev

        # return prev[0]

        