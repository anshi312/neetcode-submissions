class Solution:
    def combinationSum(self, nums, target):
        res = []

        def dfs(start, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return

            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(i, cur, total + nums[i])   # allow reuse
                cur.pop()

        dfs(0, [], 0)
        return res