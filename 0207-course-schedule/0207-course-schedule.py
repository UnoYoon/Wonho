# 선수과목을 먼저 들어야만함. [a1, b1] 위와 같이 존재하면
# b1 -> a1 이 순서로는 필수적으로 들어야 한다.
# 근데 만약 b1 -> a1 -> b1 이면  b1이 선수과목인데 a1을 듣고 b1을 다시 듣는다해도 선수과목이 뒤에 오니 문제.
# 사이클 생기면 -> False 

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses        

        for post, prev in prerequisites:
            graph[prev].append(post)
            indegree[post] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        cnt = 0

        while queue:
            course = queue.popleft()
            cnt += 1
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return cnt == numCourses