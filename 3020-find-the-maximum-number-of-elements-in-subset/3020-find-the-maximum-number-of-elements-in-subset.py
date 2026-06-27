from typing import List
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1
        if 1 in freq:
            if freq[1] % 2:
                ans = freq[1]
            else:
                ans = freq[1] - 1

        for x in list(freq.keys()):
            if x == 1:
                continue
            cur = x
            levels = 0
            while freq.get(cur, 0) >= 2:
                levels += 1
                cur *= cur
            if freq.get(cur, 0) >= 1: ans = max(ans, 2 * levels + 1)
            else: ans = max(ans, 2 * levels - 1)

        return ans