class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        minheap = [(0, src, 0)]
        best = dict()

        while minheap:
            cost, node, stops = heapq.heappop(minheap)

            if node == dst: return cost

            if stops > k: continue

            for nbh, price in graph[node]:
                new_cost = cost + price
                new_stops = stops + 1

                if (nbh, new_stops) not in best or new_cost < best[(nbh, new_stops)]:
                    best[(nbh, new_stops)] = new_cost
                    heapq.heappush(minheap, (new_cost, nbh, new_stops))
        return -1