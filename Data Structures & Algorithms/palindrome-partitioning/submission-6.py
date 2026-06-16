    #     result = []
    #     part = []

    #     def dfs(i):
    #         if i >= len(s):
    #             result.append(part.copy())
    #             return
    #         for j in range(i, len(s)):
    #             if self.isPali(s, i, j):
    #                 part.append(s[i : j+1])
    #                 dfs(j+1)
    #                 part.pop()

    #     dfs(0)
    #     return result

    # def isPali(self, s, l, r):
    #     while l < r:
    #         if s[l] != s[r]: return False
    #         l += 1
    #         r -= 1
    #     return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPali(substr):
            return substr == substr[ : : -1]

        def dfs(start, curr):
            if start == len(s):
                result.append(curr.copy())

            for end in range(start, len(s)):
                substr = s[start : end + 1]
                if isPali(substr):
                    curr.append(substr)
                    dfs(end + 1, curr)
                    curr.pop()

        dfs(0, [])
        return result