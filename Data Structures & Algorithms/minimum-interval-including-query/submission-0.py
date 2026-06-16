class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        heap = []

        result = {}

        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                heapq.heappush(heap, (right - left + 1, right))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            result[q] = heap[0][0] if heap else -1

        final_result = []
        for q in queries:
            final_result.append(result[q])

        return final_result