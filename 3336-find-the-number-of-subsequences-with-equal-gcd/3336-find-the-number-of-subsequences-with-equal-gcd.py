class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9+7
        n = len(nums)
        maxVal = max(nums)
        dp = {}
        
        def solve(i, g1, g2):
            if i == n: return 1 if(g1 > 0 and g2 > 0 and g1 == g2) else 0
            state = (i, g1, g2)
            if state in dp: return dp[state]

            res = solve(i+1, g1, g2)
            res = (res + solve(i+1, math.gcd(g1, nums[i]), g2))%MOD
            res = (res + solve(i+1, g1, math.gcd(g2, nums[i])))%MOD

            dp[state] = res
            return res

        return solve(0, 0, 0)