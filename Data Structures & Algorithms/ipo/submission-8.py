class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        
        pair = []
        for i in range(n):
            pair.append((capital[i], profits[i]))

        pair.sort()
        # (2,1) (3,5) (3,3) (4,2) (4,3)

        curr_cap = w
        heap = []
        i = 0
        for _ in range(k):
            while i < n and pair[i][0] <= curr_cap:
                heapq.heappush(heap, -pair[i][1])
                i += 1

            if not heap:
                break
            
            curr_cap += -heapq.heappop(heap)

        return curr_cap
