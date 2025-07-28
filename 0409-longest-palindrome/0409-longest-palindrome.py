# 어떠한 문자열이 주어진다.
# 문자열을 변형시켜 palindrome을 만족하는 가장 긴 문자열을 만든다. 
# 그리고 그 문자열의 길이를 출력한다. (1 <= s.length <= 2000)
# 더 쉽게 생각하면 짝수 개만 만족하면 서로 반대 위치에 놓았다고 가정을 한 것과 동일하게 생각할 수 있다.
# aabb 이렇게 원래 문자열이 있고, a가 2개, b가 2개임을 알 수 있으면 굳이 변형하지 않아도 baab 이런 식으로 만들 수 있다는 것을 알 수 있음.
# 즉, 우리는 문자열 내의 짝수 개의 같은 문자를 먼저 생각하고 남은 홀 수들을 이용해서 더해주는 느낌으로 총 output을 구할 수 있을 듯

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        has_odd = False

        for char, cnt in count.items():
            if cnt % 2 == 0:
                length += cnt
            else:
                length += cnt -1 
                has_odd = True
        
        if has_odd:
            length += 1
        
        return length
