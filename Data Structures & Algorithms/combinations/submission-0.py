class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(i, curr):
            if len(curr) == k:
                result.append(curr.copy())
                return

            for num in range(i, n + 1):
                curr.append(num)
                dfs(num + 1, curr)
                curr.pop()

        dfs(1, [])

        return result 