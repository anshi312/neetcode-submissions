class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # ----------- bottom up dp (my top down haha) ----------#

        cache = [[float('inf')] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        
        rows = len(word1) + 1
        cols = len(word2) + 1

        for i in range(cols):
            cache[0][i] = i

        for i in range(rows):
            cache[i][0] = i

        for i in range(1, rows):
            for j in range(1, cols):
                if word1[i - 1] == word2[j - 1]:
                    cache[i][j] = cache[i - 1][j - 1]
                else:
                    cache[i][j] = 1 + min(cache[i - 1][j - 1], cache[i - 1][j], cache[i][j - 1])

        return cache[-1][-1]





    # # ------------- dfs with memo --------------------------#
    #     length1 = len(word1)
    #     length2 = len(word2)

    #     memo = {}

    #     def dfs(i, j):
    #         if i == length1:
    #             return length2 - j

    #         if j == length2:
    #             return length1 - i

    #         if (i, j) in memo:
    #             return memo[(i, j)]

    #         if word1[i] == word2[j]:
    #             memo[(i, j)] = dfs(i + 1, j + 1)
    #             return memo[(i, j)]
            
    #         insert = 1 + dfs(i, j + 1)
    #         delete = 1 + dfs(i + 1, j)
    #         replace = 1 + dfs(i + 1, j + 1)
    #         memo[(i, j)] = min(insert, delete, replace)

    #         return memo[(i, j)]

    #     return dfs(0, 0)