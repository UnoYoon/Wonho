# 최대 넓이 50x50 = 2500
# sr, sc는 처음 변경되는 좌표 (sr,sc)
# sr, sc에 인접한 수 중 같은 색은 변경된다. 즉, 지금 그림은 0으로 가로막혀서 인접하지 않아서 하나의 1은 변경되지 않은 상황 ->  bfs 쓰면 될 거 같다. 
# 즉, bfs를 통해 (sr, sc) 처음 좌표를 시작으로 인접한 수에 존재하면 그 수로 변경해서 인접한 곳 다 바꾸면 종료.
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]

        if original_color == color:
            return image

        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1] 
        
        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = color

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < m and 0 <= ny < n and image[nx][ny] == original_color:
                    image[nx][ny] = color
                    queue.append((nx,ny))

        return image
                    