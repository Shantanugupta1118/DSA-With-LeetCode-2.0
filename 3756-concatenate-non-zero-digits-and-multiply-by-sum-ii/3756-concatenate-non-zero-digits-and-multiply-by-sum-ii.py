from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + int(s[i])
        prefix_val = [0] * (n + 1)
        prefix_cnt = [0] * (n + 1)
        for i in range(n):
            d = int(s[i])
            if d != 0:
                prefix_val[i + 1] = (prefix_val[i] * 10 + d) % MOD
                prefix_cnt[i + 1] = prefix_cnt[i] + 1
            else:
                prefix_val[i + 1] = prefix_val[i]
                prefix_cnt[i + 1] = prefix_cnt[i]
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        ans = []
        for l, r in queries:
            cnt = prefix_cnt[r + 1] - prefix_cnt[l]
            x_mod = (prefix_val[r + 1] - prefix_val[l] * pow10[cnt]) % MOD
            digit_sum = prefix_sum[r + 1] - prefix_sum[l]
            result = (x_mod * digit_sum) % MOD
            ans.append(result % MOD)

        return ans