class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = [False] * len(nums)
        target = len(nums) - 1
        can_reach[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= target - i:
                can_reach[i] = True
                target = i

        return can_reach[0]