class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(start, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if total > target:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                # curr.append(nums[i])
                dfs(i+1, cur + [nums[i]], total + nums[i])
                

        dfs(0, [], 0)
        return res