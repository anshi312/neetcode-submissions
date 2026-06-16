        # res = []

        # def dfs(start, cur, total):
        #     if total == target:
        #         res.append(cur.copy())
        #         return
        #     if total > target:
        #         return

        #     for i in range(start, len(nums)):
        #         cur.append(nums[i])
        #         dfs(i, cur, total + nums[i])
        #         cur.pop()

        # dfs(0, [], 0)
        # return res

class Solution:
    def combinationSum(self, nums, target):
        result = []

        def dfs(start, curr, total):
            if total == target:
                result.append(curr.copy())
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(i, curr, total + nums[i])
                curr.pop()

        dfs(0, [], 0)

        return result