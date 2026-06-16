class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False] * len(nums)

        def dfs(curr, used):
            if len(curr) == len(nums):
                result.append(curr.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                curr.append(nums[i])
                used[i] = True
                dfs(curr, used)
                curr.pop()
                used[i] = False

        dfs([], used)

        return result
