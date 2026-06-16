class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        def dfs(i, j, k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))
            if (i, j) in dp:
                return dp[(i, j)]

            dp_result = False
            if i < len(s1) and s1[i] == s3[k]:
                dp_result = dfs(i+1, j, k+1)
            if not dp_result and j< len(s2) and s2[j] == s3[k]:
                dp_result = dfs(i, j+1, k+1)
            dp[(i,j)] = dp_result
            
            return dp_result
        return dfs(0,0,0)

        # def dfs(i, j, k):
        #     if k == len(s3):
        #         return (i == len(s1)) and (j == len(s2))
        #     if i < len(s1) and s1[i] == s3[k]:
        #         if dfs(i+1, j, k+1): return True
        #     if j< len(s2) and s2[j] == s3[k]:
        #         if dfs(i, j+1, k+1): return True

        #     return False

        # return dfs(0,0,0)