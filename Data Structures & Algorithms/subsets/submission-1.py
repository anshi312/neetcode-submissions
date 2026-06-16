class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            subsets = []
            for subset in result:
                subsets.append(subset + [num])
            result.extend(subsets)
        return result