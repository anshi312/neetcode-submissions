        # nums.sort()
        # res = []

        # def dfs(start, cur, total):
        #     if total == target:
        #         res.append(cur[:])
        #         return
        #     if total > target:
        #         return

        #     for i in range(start, len(nums)):
        #         if i > start and nums[i] == nums[i-1]:
        #             continue
        #         cur.append(nums[i])
        #         dfs(i+1, cur, total + nums[i])
                

        # dfs(0, [], 0)
        # return res

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(start, curr, total):
            if total == target:
                result.append(curr.copy())
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                dfs(i + 1, curr + [nums[i]], total + nums[i])

        dfs(0, [], 0)

        return result