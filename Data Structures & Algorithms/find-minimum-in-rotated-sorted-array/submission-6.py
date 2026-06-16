        # left = 0
        # right = len(nums) - 1
        # res = nums[0]
        # while left <= right:
        #     if nums[left] < nums[right]:
        #         res = min(res, nums[left])

        #     mid = (left+right)//2
        #     res = min(res, nums[mid])
        #     if nums[mid] >= nums[left]:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return res

# 3 4 5 6 1 2

# 7. 0. 1 2. 3 4 5 6

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid

        return nums[left]