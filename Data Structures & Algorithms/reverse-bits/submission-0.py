class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):     # as 32-bit was given
            bit = (n >> i) & 1
            result += (bit << (31 - i))

        return result