class Solution:
    def decodeString(self, s: str) -> str:

        # 2[a3[b]]c
        # when [ --> save current result
        # when ] --> repear current str and attack it to result

        stack = []
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif char == ']':
                prev_str, prev_num = stack.pop()
                curr_str = prev_str + curr_str * prev_num
            else:
                curr_str += char

        return curr_str