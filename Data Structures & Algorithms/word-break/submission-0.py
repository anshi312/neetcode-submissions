class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)

        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for word in wordSet:
                lw = len(word)
                if i >= lw and s[i-lw:i] == word and dp[i-lw]:
                    dp[i] = True
                    break
        return dp[-1]