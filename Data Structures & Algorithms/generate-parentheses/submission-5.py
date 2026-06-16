        # stack =[]
        # result = []

        # def backtrack(openx, closedx):
        #     if openx == closedx == n:
        #         result.append("".join(stack))
        #         return

        #     if openx < n:
        #         stack.append("(")
        #         backtrack(openx + 1, closedx)
        #         stack.pop()

        #     if closedx < openx:
        #         stack.append(")")
        #         backtrack(openx, closedx + 1)
        #         stack.pop()
                
        # backtrack(0, 0)
        # return result

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(curr, open_cnt, closed_cnt):
            if open_cnt == closed_cnt == n:
                result.append("".join(curr))
                return

            if open_cnt < n:
                curr.append('(')
                dfs(curr, open_cnt + 1, closed_cnt)
                curr.pop()

            if closed_cnt < open_cnt:
                curr.append(')')
                dfs(curr, open_cnt, closed_cnt + 1)
                curr.pop()

        dfs([], 0, 0)
        # result = ''.join(result)
        return result
