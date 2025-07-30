# 음수면 minus 기호로 팰린드롬수가 될 수 없다. 
# 0, 자연수 palindrome 찾기

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # 언제 끝나냐? x = 12 , reversed_half = 123
        
        return x == reversed_half or x == reversed_half // 10