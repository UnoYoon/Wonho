# 1이 연결되어 있는 상하좌우는 같은 섬으로 취급
# 그러면 같은 섬으로 취급을 다 한 다음에 섬 탐색

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            visited[x][y] = True

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    dx, dy = x + dx, y + dy
                    if 0 <= dx < rows and 0 <= dy < cols:
                        if not visited[dx][dy] and grid[dx][dy] == "1":
                            visited[dx][dy] = True
                            queue.append((dx, dy))
        
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    count += 1

        return count