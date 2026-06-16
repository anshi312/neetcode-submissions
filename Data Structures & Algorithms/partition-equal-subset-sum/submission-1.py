class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True

        return dp[target]

#######################################

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        def dfs(idx, curr_sum):
            if curr_sum == target:
                return True

            if curr_sum > target or idx >= n:
                return False

            take = dfs(idx + 1, curr_sum + nums[idx])
            not_take = dfs(idx + 1, curr_sum)

            return take or not_take

        return dfs(0, 0)