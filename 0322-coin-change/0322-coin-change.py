# amount // coins 큰 수 
# 있으면 통과 없으면 다음 큰 수 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] +  1)

        return dp[amount] if dp[amount] != float('inf') else -1