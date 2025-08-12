class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(start, remaining):
            if not remaining:
                result.append(start[:])
                return
            
            for i in range(len(remaining)):
                start.append(remaining[i])
                backtracking(start, remaining[:i] + remaining[i + 1:])
                start.pop()

        backtracking([], nums)
        return result 
