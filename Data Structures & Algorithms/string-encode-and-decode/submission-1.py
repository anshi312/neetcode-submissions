class Solution:

# Hell#o World
# 6#Hell#o 5#World
# 01234567 89

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + '#' + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            result.append(s[j + 1 : length + 1 + j])
            i = 1 + j + length

        return result






























# --------- encode ----------- #
        # result = ""

        # for s in strs:
        #     result += str(len(s)) + "#" + s
        # return result

# --------- decode ------------ #
        # result = []
        # i = 0

        # while i < len(s):
        #     j = i
        #     while s[j]!="#":
        #         j += 1
        #     length = int(s[i:j])
        #     result.append(s[j+1 : 1+j+length])
        #     i = j+1+length

        # return result