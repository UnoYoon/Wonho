# 문자열을 앞으로 탐색하면서 공통 부분을 찾으면 가장 긴 공통 부분을 출력하는 문제
# 공통 부분이 존재하지 않다면 ""을 출력하라.
# strs[0] strs[1] strs[2]--- 200개까지 계속해서 비교
 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_len = min(len(word) for word in strs)
        result = ""

        for i in range(min_len):
            char = strs[0][i]
            for word in strs[1:]:
                if word[i] != char:
                    return result
            result += char
        return result