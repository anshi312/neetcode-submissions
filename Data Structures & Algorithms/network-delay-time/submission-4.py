class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))

        distance = [float('inf')] * (n + 1)
        distance[0] = 0
        distance[k] = 0

        heap = [(0, k)]
        
        while heap:
            curr_time, node = heapq.heappop(heap)

            if curr_time > distance[node]:
                continue

            for nbh, time in graph[node]:
                new_time = curr_time + time

                if new_time < distance[nbh]:
                    distance[nbh] = new_time
                    heapq.heappush(heap, (new_time, nbh))

        max_time = max(distance)

        return max_time if max_time != float('inf') else -1