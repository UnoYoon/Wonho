from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[-1] * n for _ in range(m)] # 이거 물어보기
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1] # 이 부분도 순서 상,하,좌,우 지켜야하는지 물어보기

        while queue:
            x, y = queue.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
        return dist