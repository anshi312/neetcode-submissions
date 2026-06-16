class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {}
        window = {}

        # Build counts for s1 and the first window in s2
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1

        # Sliding window
        matches = 0
        for c in s1Count:
            if s1Count.get(c, 0) == window.get(c, 0):
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == len(s1Count):
                return True

            # Add new right char
            rc = s2[r]
            window[rc] = window.get(rc, 0) + 1
            if rc in s1Count:
                if window[rc] == s1Count[rc]:
                    matches += 1
                elif window[rc] == s1Count[rc] + 1:
                    matches -= 1

            # Remove old left char
            lc = s2[l]
            window[lc] -= 1
            if lc in s1Count:
                if window[lc] == s1Count[lc]:
                    matches += 1
                elif window[lc] == s1Count[lc] - 1:
                    matches -= 1

            l += 1

        return matches == len(s1Count)