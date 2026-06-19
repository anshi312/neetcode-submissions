class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        length = 0
        left = right = 0
        for right in range(len(s)):
            char = s[right]
            while char in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(char)
            right += 1
            length = max(length, (right - left))

        return length