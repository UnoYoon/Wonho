# n까지의 각 이진수를 더해서 배열로 출력하기
# 그 전 배열을 가지고 있으면 그 다음 값은 그냥 거기에 추가하기만 하면 되잖아.
# 예를 들면 1, 2, 3, 4 가지고 있었어. n = 4
# n = 5 -> 5일 때만 갱신 해주는 식으로 하면 된다. 
# 1. 이진수로 변환, 이진수 쪼개서 각 자리 더하기 그리고 배열에 추가, 마지막으로 배열 리턴


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            binary_str = str(bin(i)[2:])
            digits = [int(digit) for digit in binary_str]
            total = sum(digits)
            result.append(total)
        return result