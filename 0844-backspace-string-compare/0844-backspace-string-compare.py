# '#'을 입력받으면 그 전 문자 값이 사라짐. 
# 이후 최종 문자 s,t를 비교하여 같은지 체

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)
        
        return build(s) == build(t)