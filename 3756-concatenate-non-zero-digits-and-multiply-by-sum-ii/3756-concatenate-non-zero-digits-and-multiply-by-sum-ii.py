from typing import List
import numpy as np

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # --- Vectorized digit extraction ---
        digits = np.frombuffer(s.encode(), dtype=np.uint8).astype(np.int64) - 48
        nonzero_mask = digits != 0

        # --- prefix_sum (vectorized) ---
        prefix_sum = np.zeros(n + 1, dtype=np.int64)
        np.cumsum(digits, out=prefix_sum[1:])

        # --- prefix_cnt (vectorized) ---
        prefix_cnt = np.zeros(n + 1, dtype=np.int64)
        np.cumsum(nonzero_mask, out=prefix_cnt[1:])
        max_cnt = int(prefix_cnt[-1])

        # --- Precompute power tables (unavoidable O(n) scalar loop, but trivial ops) ---
        pow10 = np.empty(n + 1, dtype=np.int64)
        pow10[0] = 1
        p = 1
        for i in range(1, n + 1):
            p = (p * 10) % MOD
            pow10[i] = p

        inv10 = pow(10, MOD - 2, MOD)
        pow_inv10 = np.empty(max_cnt + 1, dtype=np.int64)
        pow_inv10[0] = 1
        p = 1
        for i in range(1, max_cnt + 1):
            p = (p * inv10) % MOD
            pow_inv10[i] = p

        # --- b_j = d_j * inv10^(cnt_j) for nonzero digits, else 0 (fully vectorized) ---
        cnt_at_j = prefix_cnt[1:]  # cnt after including position j (1-indexed alignment)
        gathered_inv = pow_inv10[cnt_at_j]
        b = np.where(nonzero_mask, (digits * gathered_inv) % MOD, 0)

        # --- prefix_B: cumulative sum (vectorized, safe from overflow since terms < MOD) ---
        prefix_B = np.zeros(n + 1, dtype=np.int64)
        np.cumsum(b, out=prefix_B[1:])
        prefix_B %= MOD

        # --- prefix_val = pow10[cnt_i] * prefix_B[i] mod MOD (vectorized) ---
        prefix_val = (pow10[prefix_cnt] * prefix_B) % MOD

        # --- Vectorized query processing ---
        q = np.asarray(queries, dtype=np.int64)
        l = q[:, 0]
        r = q[:, 1]
        r1 = r + 1

        cnt = prefix_cnt[r1] - prefix_cnt[l]
        x_mod = (prefix_val[r1] - prefix_val[l] * pow10[cnt]) % MOD
        digit_sum = prefix_sum[r1] - prefix_sum[l]
        result = (x_mod * digit_sum) % MOD

        return result.tolist()