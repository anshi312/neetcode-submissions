class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [0]*len(nums)
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
        #     res[i] = prod
        # return res

        # 1 2 4 6
        # prefix --> 1 1 2 8
        # posfix --> 48 24 6 1 
        # result --> 48 24 12 8

        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix 
            postfix *= nums[i]

        return result