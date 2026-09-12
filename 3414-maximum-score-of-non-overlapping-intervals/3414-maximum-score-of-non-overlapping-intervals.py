from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        events = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)], key=lambda x: x[1])
        
        rights = [x[1] for x in events]
        
        dp = [[(0, ())] * (n + 1) for _ in range(5)]
        
        for i in range(1, n + 1):
            l, r, w, orig_idx = events[i - 1]
            
            prev_idx = bisect_left(rights, l) - 1
            
            for k in range(1, 5):
                best_w, best_tuple = dp[k][i - 1]
                
                prev_w, prev_tuple = dp[k - 1][prev_idx + 1]
                cand_w = prev_w + w
                cand_tuple = tuple(sorted(prev_tuple + (orig_idx,)))
                
                if cand_w > best_w:
                    best_w, best_tuple = cand_w, cand_tuple
                elif cand_w == best_w and cand_w > 0:
                    if best_tuple == () or cand_tuple < best_tuple:
                        best_tuple = cand_tuple
                
                dp[k][i] = (best_w, best_tuple)
                
        return list(dp[4][n][1])