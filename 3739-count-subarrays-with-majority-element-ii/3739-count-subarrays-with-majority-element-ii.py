from typing import List
from collections import defaultdict

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        freq = defaultdict(int)
        freq[0] = 1         
        prefix = 0
        less_count = 0       
        count = 0

        for num in nums:
            last_val = prefix
            prefix += 1 if num == target else -1
            if prefix > last_val:
                less_count += freq[prefix - 1]  
            else:
                less_count -= freq[prefix]

            count = count + less_count
            freq[prefix] += 1

        return count