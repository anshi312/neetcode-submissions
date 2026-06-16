class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums.sort()

        for num in nums:
            temp_subsets = []   

            for subset in result:
                temp_subsets.append(subset + [num])
            
            for subset in temp_subsets:
                if subset not in result: 
                    result.append(subset)
            
        return result

        


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = [[]]
#         for num in nums:
#             subsets = []
#             for subset in result:
#                 subsets.append(subset + [num])
#             result.extend(subsets)
#         return result