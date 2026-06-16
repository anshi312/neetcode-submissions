class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0

        heap = [(0, 0, 0)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while heap:
            curr_effort, row, col = heapq.heappop(heap)

            if row == rows - 1 and col == cols - 1:
                return curr_effort

            for dr, dc in directions:
                new_r = row + dr
                new_c = col + dc

                if 0 <= new_r < rows and 0 <= new_c < cols:
                    curr_diff = abs(heights[row][col] - heights[new_r][new_c])
                    new_effort = max(curr_effort, curr_diff)

                    if new_effort < effort[new_r][new_c]:
                        effort[new_r][new_c] = new_effort
                        heapq.heappush(heap, (new_effort, new_r, new_c))

        return 0