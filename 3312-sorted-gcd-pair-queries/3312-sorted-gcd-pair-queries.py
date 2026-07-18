import math
from typing import List
from itertools import accumulate
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_num = max(nums)
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1
        count_divisible = [0] * (max_num + 1)
        for d in range(1, max_num + 1):
            for multiple in range(d, max_num + 1, d):
                count_divisible[d] += freq[multiple]
        exact_gcd = [0] * (max_num + 1)
        for g in range(max_num, 0, -1):
            total_divisible_pairs = (count_divisible[g] * (count_divisible[g] - 1)) // 2
            for multiple in range(2 * g, max_num + 1, g):
                total_divisible_pairs -= exact_gcd[multiple]
            exact_gcd[g] = total_divisible_pairs
        prefix_sums = list(accumulate(exact_gcd))
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans
