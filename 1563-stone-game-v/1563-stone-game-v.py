class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        
        # Prefix sum array for O(1) sum lookups
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
            
        def get_sum(l: int, r: int) -> int:
            return pref[r + 1] - pref[l]

        dp = [[0] * n for _ in range(n)]
        
        # max_left[i][j] stores max_{i <= k <= j} (get_sum(i, k) + dp[i][k])
        max_left = [[0] * n for _ in range(n)]
        # max_right[i][j] stores max_{i <= k <= j} (get_sum(k, j) + dp[k][j])
        max_right = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]

        for i in range(n - 1, -1, -1):
            mid = i
            for j in range(i + 1, n):
                # Advance mid so that get_sum(i, mid) is the largest sum <= get_sum(mid + 1, j)
                while mid < j and get_sum(i, mid) < get_sum(mid + 1, j):
                    mid += 1
                
                # Option 1: splits k where left_sum < right_sum (k in [i, mid - 1])
                res = 0
                if mid > i:
                    res = max(res, max_left[i][mid - 1])
                
                # Option 2: splits k where left_sum > right_sum (k in [mid + 1, j - 1])
                if mid < j:
                    res = max(res, max_right[mid + 1][j])
                
                # Option 3: exact equality split at mid (left_sum == right_sum)
                if get_sum(i, mid) == get_sum(mid + 1, j):
                    res = max(res, max_left[i][mid])
                    
                dp[i][j] = res
                
                total = get_sum(i, j)
                max_left[i][j] = max(max_left[i][j - 1], total + dp[i][j])
                max_right[i][j] = max(max_right[i + 1][j], total + dp[i][j])

        return dp[0][n - 1]