from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digitCounts = Counter(digits)
        validCount = 0

        for num in range(100, 1000, 2):
            d1 = num//100
            d2 = (num//10)%10
            d3 = num%10

            reqCounts = Counter([d1, d2, d3])
            if all(digitCounts[d] >= reqCounts[d] for d in reqCounts):
                validCount += 1
        return validCount