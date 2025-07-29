# 로마 글자 -> 정수형으로 변환
# IV -> 작은 숫자가 큰 숫자 앞에 존재하면 뺀다.
# 그외에는 두 숫자가 만나면 다 더한다.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        total = 0
        prev = 0

        for c in reversed(s): 
            value = roman[c]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value

        return total

        # IV -> 1. value = 1 prev = value = 1 2. value = 4, prev = 1 -> 4 + 1 = 5