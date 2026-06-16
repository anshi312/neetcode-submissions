class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = cols = len(grid)
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = [(grid[0][0], 0, 0)]

        while heap:
            curr_height, row, col = heapq.heappop(heap)

            if (row, col) in visited:
                continue

            visited.add((row, col))

            if row == rows - 1 and col == cols - 1:
                return curr_height
            
            for dr, dc in directions:
                new_r = row + dr
                new_c = col + dc

                if (0 <= new_r < rows and 0 <= new_c < cols) and (new_r, new_c) not in visited:
                    new_max = max(curr_height, grid[new_r][new_c])
                    heapq.heappush(heap, (new_max, new_r, new_c))

        return 0