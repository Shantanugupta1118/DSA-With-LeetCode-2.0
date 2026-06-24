import numpy as np

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        CHUNK = 8

        def mat_mul(A, B):
            C = np.zeros((m, m), dtype=np.int64)
            for start in range(0, m, CHUNK):
                end = min(start + CHUNK, m)
                C += A[:, start:end] @ B[start:end, :]
                C %= MOD
            return C

        def mat_pow(M, p):
            result = np.eye(m, dtype=np.int64)
            while p > 0:
                if p & 1:
                    result = mat_mul(result, M)
                M = mat_mul(M, M)
                p >>= 1
            return result

        # Peak: next[x] = sum of dp[y] for y < x
        P = np.array([[1 if j < i else 0 for j in range(m)] for i in range(m)], dtype=np.int64)
        # Valley: next[x] = sum of dp[y] for y > x
        V = np.array([[1 if j > i else 0 for j in range(m)] for i in range(m)], dtype=np.int64)

        # Transitions: P, V, P, V, ... (n-1 total)
        # Pair them as VP (P first, then V) = one two-step matrix
        VP = mat_mul(V, P)

        steps = n - 1
        pairs, remainder = steps // 2, steps % 2

        dp = np.ones(m, dtype=np.int64)
        if pairs > 0:
            dp = mat_pow(VP, pairs) @ dp % MOD
        if remainder:
            dp = P @ dp % MOD

        return int(dp.sum() % MOD) * 2 % MOD