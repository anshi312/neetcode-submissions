# racecariscar
# race car is car
# racecar is car

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []

        def dfs(start, words):
            if start == len(s):
                result.append(" ".join(words))
                return

            for i in range(start, len(s)):
                curr = s[start : i + 1]

                if curr in wordDict:
                    words.append(curr)
                    dfs(i + 1, words)
                    words.pop()
                    

        dfs(0, [])

        return result