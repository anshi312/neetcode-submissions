class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        result = 0
        for num in nums:
            if (num - 1) not in num_set:
                length = 0
                while (num + length) in num_set:
                    length += 1
                    result = max(length, result)
        
        return result

        # ------- sorting ---------- #
        # if not nums:
        #     return 0

        # nums.sort()
        # streak = 1
        # longest = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]: continue

        #     if nums[i] == nums[i-1] + 1: streak+= 1
        #     else:
        #         longest = max(longest, streak)
        #         streak = 1

        # return max(longest, streak)

        # ---------- set --------- #

        # numSet = set(nums)
        # longest = 0

        # for n in nums:
        #     if (n-1) not in numSet:
        #         length = 0
        #         while (n+length) in numSet:
        #             length += 1
        #         longest = max(length, longest)
        
        # return longest
