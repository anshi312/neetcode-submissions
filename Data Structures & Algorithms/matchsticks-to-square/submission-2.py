class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        side = sum(matchsticks) // 4
        if max(matchsticks) > side:
            return False

        matchsticks.sort(reverse=True)

        sides = [0, 0, 0, 0]
        def dfs(i, sides):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] > side:
                    continue

                sides[j] += matchsticks[i]

                if dfs(i + 1, sides):
                    return True

                sides[j] -= matchsticks[i]

                if sides[j] == 0:
                    break

            return False

        return dfs(0, sides)

        

                


            
                
