class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = []
        for i in range(len(tasks)):
            enqueue_t, process_t = tasks[i]
            indexed_tasks.append((enqueue_t, process_t, i))

        n = len(tasks)
        indexed_tasks.sort()

        result = []
        heap = []

        time = 0
        i = 0

        while i < n or heap:
            if not heap and time < indexed_tasks[i][0]:
                time = indexed_tasks[i][0]

            while i < n and indexed_tasks[i][0] <= time:
                enqueue_t, process_t, idx = indexed_tasks[i]
                heapq.heappush(heap, (process_t, idx))
                i += 1

            process_time, idx = heapq.heappop(heap)
            time += process_time
            result.append(idx)

        return result
