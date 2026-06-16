class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack =[]
        result = []
        def backtrack(openx, closedx):
            if openx == closedx == n:
                result.append("".join(stack))
                return
            if openx < n:
                stack.append("(")
                backtrack(openx + 1, closedx)
                stack.pop()
            if closedx < openx:
                stack.append(")")
                backtrack(openx, closedx + 1)
                stack.pop()
        backtrack(0, 0)
        return result