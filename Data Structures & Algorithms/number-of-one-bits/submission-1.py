class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += 1 if n & 1 else 0
            n >>= 1
        return result