class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for char in operations:
            if char == '+':
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif char =='C':
                stack.pop()
            elif char == 'D':
                stack.append(2 * int(stack[-1]))
            else:
                stack.append(int(char))

        return sum(stack)