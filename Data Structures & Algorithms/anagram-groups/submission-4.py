class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # result = []

        anagram_map = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)

            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(s)

        return list(anagram_map.values())

        