# 1. 모든 오렌지를 썩게 만들지
# 2. 모든 오렌지를 썩게 만들지 못할 때 : -1 출력 (오렌지가 싱싱한게 하나 이상 남았다는 뜻)
# 넓이가 100인 그리드를 탐색하는 방법 : BFS
# 썩은 오렌지 : 2, 썩지 않은 오렌지 : 1, 오렌지가 존재하지 않는 칸 : 0

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        while queue:
            x, y, minutes = queue.popleft()
            time = max(time, minutes)

            for dx, dy in directions:
                dx, dy = dx + x, dy + y
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                    grid[dx][dy] = 2
                    fresh -= 1
                    queue.append((dx, dy, minutes + 1)) 
        
        return time if fresh == 0 else -1