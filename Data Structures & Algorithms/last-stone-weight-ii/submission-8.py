# sum_A + sum_B = total sum
# sum_A - sum_B = ???? lets say x
# 2 sum_A = total + x
# x = total - (2 * sum_A)
# for minimum x --> total - () should be minimum
# thus sum_A should be as close as total // 2


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        #------- optimised ----------#
        # store possible sum values, then for next stones, store adding their value
        # to the possible sum values or subtracting them to possible sum values

        possible = {0}
        
        for stone in stones:
            new_set = set()
            for s in possible:
                new_set.add(s + stone)
                new_set.add(s - stone)
            possible = new_set
        
        return min(abs(x) for x in possible)

        #------- elite brute force - more understandable ------#
        # to every stone either add it or subtract it from curr sum


        # n = len(stones)

        # def dfs(i, curr_sum):
        #     if i == n:
        #         return abs(curr_sum)

        #     return min(
        #         dfs(i+1, curr_sum + stones[i]),
        #         dfs(i+1, curr_sum - stones[i])
        #     )

        # return dfs(0, 0)


        #------ dfs solution TLE! 23/24 TCs still passed -----#
        
        # n = len(stones)

        # def dfs(i, sumA, sumB):
        #     if i == n:
        #         return abs(sumA - sumB)

        #     takeA = dfs(i+1, sumA + stones[i], sumB)
        #     takeB = dfs(i+1, sumA, sumB + stones[i])

        #     return min(takeA, takeB)

        # return dfs(0, 0, 0)

        #-----wrong approach passed 3/24 TCs lol-----#

        # stones_set = set(stones)

        # while len(stones_set) > 1:
        #     min_wt = min(stones_set)
        #     max_wt = max(stones_set)

        #     diff = max_wt - min_wt
        #     stones_set.remove(min_wt)
        #     stones_set.remove(max_wt)
        #     stones_set.add(diff)

        # return stones_set.pop()