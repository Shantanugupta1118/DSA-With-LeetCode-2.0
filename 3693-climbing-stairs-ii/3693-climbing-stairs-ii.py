class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for j in range(1, n+1):
            for i in range(max(0, j-3), j):
                jumpCost = costs[j-1]+(j-i)**2
                dp[j] = min(dp[j], dp[i]+jumpCost)
        return dp[n]