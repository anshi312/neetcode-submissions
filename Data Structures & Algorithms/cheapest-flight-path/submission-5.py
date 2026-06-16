class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for source, dest, price in flights:
            graph[source].append((dest, price))

        visited = dict()

        heap = [(0, src, 0)]

        while heap:
            curr_cost, curr_src, stops = heapq.heappop(heap)

            if curr_src == dst:
                return curr_cost

            if stops > k:
                continue

            if (curr_src in visited and visited[curr_src] <= stops):
                continue

            visited[curr_src] = stops

            for nbh, price in graph[curr_src]:
                heapq.heappush(heap, (curr_cost + price, nbh, stops + 1))

        return -1