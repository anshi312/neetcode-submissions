class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_index = {}
        for i, char in enumerate(s):
            end_index[char] = i

        result = []
        size = 0
        curr_end = 0
        for i, char in enumerate(s):
            curr_end = max(curr_end, end_index[char])
            size += 1

            if i == curr_end:
                result.append(size)
                size = 0

        return result