class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(split_sum):
            total = 0
            arrays = 1
            for num in nums:
                if total + num > split_sum:
                    total = 0
                    arrays += 1
                total += num
            return arrays <= k

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left