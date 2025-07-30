# 음수면 minus 기호로 팰린드롬수가 될 수 없다. 
# 0, 자연수 palindrome 찾기

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        if x == 0:
            return True
        
        reverse_x = ''.join(reversed(str(x)))
        n = str(x)

        if reverse_x == n :
            return True
        
        return False