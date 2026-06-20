class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t = {}
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
        
        need = len(count_t)
        have = 0

        window = float('inf')
        best_window = [-1, -1]
        
        left = 0
        count_s = {}
        for right in range(len(s)):
            char = s[right]
            count_s[char] = 1 + count_s.get(char, 0)
            
            if char in count_t and count_t[char] == count_s[char]:
                have += 1

            while have == need:
                curr_window = right - left + 1
                if curr_window < window:
                    window = curr_window
                    best_window = [left, right]

                count_s[s[left]] -= 1
                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1

        if best_window == float('inf'):
            return ""
        else:
            return s[best_window[0] : best_window[1] + 1]

        