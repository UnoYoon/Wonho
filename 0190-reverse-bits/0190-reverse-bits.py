# n을 받는다. -> 이진수로 변환
# 이진수 -> 문자열로 변환 -> 리버스 적용 -> 정수 -> 십진수로 변환

class Solution:
    def reverseBits(self, n: int) -> int:
        binary_n = bin(n)[2::].zfill(32) # 32비트를 고정비트로 만듦 
                                         # (원래는 0을 없애는 경우가 다 반수)
        reversed_binary_n = ''.join(reversed(str(binary_n)))
        x = int(reversed_binary_n, 2)
        
        return x
        