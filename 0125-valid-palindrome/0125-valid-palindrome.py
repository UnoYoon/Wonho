# 즉, palindrome을 찾는데 그 안에 있는 다른 부호들은 신경 안쓴다.
# 알파벳을 제외한 나머지 문자는 다 삭제해서 만듦
# 팰린드롬 검사: 홀수든 짝수든 맨 앞 - 맨 뒤 이런 식으로 가운데 문자까지 검사 하면 다 검사 가능 O(n) 시간동안 다 검사 가능하다. 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = [i.lower() for i in s if i.isalnum()]
        c = ''.join(c)
        for x in range(len(c) // 2) :
            if c[x] != c[len(c)-x - 1]:
                return False
        return True


# 예외 상황 : "0P" -> "P"가 되고 true가 처리된다.