class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9+7
        dp = [1]*(r+1)
    
        for i in range(1, n):
            next_dp = [1]*(r+1)

            if i%2 == 1:
                pre = 0
                for x in range(l, r+1):
                    next_dp[x] = pre
                    pre = (pre+dp[x])%MOD
            else:
                suff = 0
                for x in range(r, l-1, -1):
                    next_dp[x] = suff
                    suff = (suff+dp[x])%MOD
            dp = next_dp

        count = 0
        for x in range(l, r+1):
            count = (count + dp[x])%MOD
        return (count*2)%MOD