class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_str = str(bin(n)[2:])
        digits = [int(digit) for digit in binary_str]
        
        result = 0
        for i in range(len(digits)):
            result += digits[i]
        
        return result