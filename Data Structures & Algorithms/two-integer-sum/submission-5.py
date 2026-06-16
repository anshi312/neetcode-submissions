class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in index_map:
                return [index_map[diff], i]
            index_map[n] = i
        return []