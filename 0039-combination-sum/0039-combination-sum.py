# 1. candidates에 있는 수들을 활용하여 target을 만들 수 있는 경우를 다 출력하는 문제
# 2. if 만들 수 없는 target이라면, 빈 배열 []을 출력합니다.
# 3. 더하는 조건만 생각하면 된다. 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        def dfs(path, start, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(path, i, total + candidates[i])
                path.pop()
            
        dfs([], 0, 0)
        return result