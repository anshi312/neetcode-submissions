class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return [[]]

        # perms = self.permute(nums[1:])
        # res = []
        # for p in perms:
        #     for i in range(len(p)+1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)
        # return res

        perms = [[]]

        for n in nums:
            new = []
            for p in perms:
                for i in range(len(p)+1):
                    pcopy = p.copy()
                    pcopy.insert(i, n)
                    new.append(pcopy)
            perms = new
        return perms