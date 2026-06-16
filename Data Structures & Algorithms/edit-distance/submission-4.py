class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1 = len(word1)
        length2 = len(word2)

        memo = {}

        def dfs(i, j):
            if i == length1:
                return length2 - j

            if j == length2:
                return length1 - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            
            insert = 1 + dfs(i, j + 1)
            delete = 1 + dfs(i + 1, j)
            replace = 1 + dfs(i + 1, j + 1)
            memo[(i, j)] = min(insert, delete, replace)

            return memo[(i, j)]

        return dfs(0, 0)