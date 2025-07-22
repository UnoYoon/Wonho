# 1. 앞에서 사고 뒤에서 판다. (이건 불변)
# 2. 가치 : 1 -> 가치 : 6  즉, 최소, 최대를 구하고 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10000
        max_profit= 0 # example 2를 생각하면 0을 안할 수가 없다. 음수가 나오더라도 0으로 출력하길 원함.
        for i in prices :
            min_price = min(min_price, i)
            max_profit = max(max_profit, i - min_price)
        return max_profit
