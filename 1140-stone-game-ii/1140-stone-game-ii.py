class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        ssum = [0]*(n+1)

        for i in range(n-1, -1, -1):
            ssum[i] = ssum[i+1] + piles[i]

        @lru_cache(None)
        def dfs(i, m):
            if i+2*m>=n: return ssum[i]

            maxStones = 0
            for x in range(1, 2*m+1):
                current = ssum[i] - dfs(i+x, max(m, x))
                maxStones = max(maxStones, current)
            return maxStones
        return dfs(0, 1)