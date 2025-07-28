# 계단수가 주어질 때 계단을 다 오르는 방법 가짓수 구하기
# 한 칸 or 두 칸만 오를 수 있다. 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]