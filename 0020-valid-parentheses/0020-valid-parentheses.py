# 1. 전체 01/ 23/ 45 이런 식으로 붙어있든지
# 2. 05/ 14 / 23 이런 식으로 포괄하던지
# 3. {[]()} 둘 다 포함하든지 05 / 12/ 34 -> 즉, 1 or 2를 다 만족하면 문제는 풀린다. 
# 이러면 조금 더 수월 -> ( : count + 1 , ) : count - 1 그런데 아직 ([)] 1, 1, 0, 0 나의 괄호가 끝났는데 다른 애가 아직 1이면 그건 안되는 것. 즉, 내 1이 안끝났는데 새로운 1이 등장하면 그 새로운 1이 0이 된 후 나의 1이 0이 되어야 true
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack or stack[-1] != pair[char] :
                    return False
                stack.pop()

        return not stack