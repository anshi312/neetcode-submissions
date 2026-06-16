class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        # visited sets for each ocean
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]

        q_pac = deque()
        q_atl = deque()

        # 1. Initialize BFS with all Pacific-border cells (top row + left col)
        for c in range(cols):
            q_pac.append((0, c))
            pac[0][c] = True
        for r in range(rows):
            q_pac.append((r, 0))
            pac[r][0] = True

        # 2. Initialize BFS with all Atlantic-border cells (bottom row + right col)
        for c in range(cols):
            q_atl.append((rows - 1, c))
            atl[rows - 1][c] = True
        for r in range(rows):
            q_atl.append((r, cols - 1))
            atl[r][cols - 1] = True

        # Helper function: BFS for one ocean
        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()

                # explore 4 neighbors
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc

                    # bounds check
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue

                    # skip visited cells
                    if visited[nr][nc]:
                        continue

                    # reverse flow condition: neighbor height >= current height
                    if heights[nr][nc] < heights[r][c]:
                        continue

                    visited[nr][nc] = True
                    queue.append((nr, nc))

        # 3. BFS from Pacific and Atlantic
        bfs(q_pac, pac)
        bfs(q_atl, atl)

        # 4. Collect cells reachable to both oceans
        result = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    result.append([r, c])

        return result