class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # result = [[]]
        # for num in nums:
        #     subsets = []
        #     for subset in result:
        #         subsets.append(subset + [num])
        #     result.extend(subsets)
        # return result

        result = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result