class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordSet = set(wordDict)
        # n = len(s)  # n = 8

        # dp = [False] * (n+1)    # dp = [T F F  F F F  F F F]
        # dp[0] = True

        # for i in range(1, n+1):
        #     for word in wordSet:
        #         lw = len(word)
        #         if i >= lw and s[i-lw:i] == word and dp[i-lw]:
        #             dp[i] = True
        #             break
        # return dp[-1]


        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet:
                    if dfs(end):
                        memo[start] = True
                        return True

            memo[start] = False
            return False

        return dfs(0)