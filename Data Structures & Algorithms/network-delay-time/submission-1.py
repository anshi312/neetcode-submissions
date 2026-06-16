class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        dist = {i: float('inf') for i in range (1, n+1)}
        dist[k] = 0

        minheap = [(0, k)]
        
        while minheap:
            currtime, node = heapq.heappop(minheap)

            if currtime > dist[node]:
                continue

            for nbh, time_needed in graph[node]:
                newtime = currtime + time_needed

                if newtime < dist[nbh]:
                    dist[nbh] = newtime
                    heapq.heappush(minheap, (newtime, nbh))

        max_time = max(dist.values())

        return max_time if max_time < float('inf') else -1