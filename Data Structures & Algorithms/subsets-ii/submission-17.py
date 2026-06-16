class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(i, curr):
            if i > len(nums):
                return
            result.append(curr.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                curr.append(nums[j])
                dfs(j + 1, curr)
                curr.pop()
                #dfs(i + 1, curr)

        dfs(0, [])
        return result
            
            




        # Solution edited from Subset I question. Time Complexity: O(n^3)

        # result = [[]]
        # nums.sort()

        # for num in nums:
        #     temp_subsets = []   

        #     for subset in result:
        #         temp_subsets.append(subset + [num])
            
        #     for subset in temp_subsets:
        #         if subset not in result: 
        #             result.append(subset)
            
        # return result

        #         result = []

        # subset = []
        # def dfs(i):
        #     if i >= len(nums):
        #         result.append(subset.copy())
        #         return
            
        #     subset.append(nums[i])
        #     dfs(i + 1)
        #     subset.pop()
        #     dfs(i + 1)

        # dfs(0)
        # return result