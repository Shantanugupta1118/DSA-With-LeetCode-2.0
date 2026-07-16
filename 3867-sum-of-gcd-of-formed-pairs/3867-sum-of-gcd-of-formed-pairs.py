class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        maxVal = 0

        for nm in nums:
            maxVal = max(maxVal, nm)
            prefixGcd.append(math.gcd(nm, maxVal))


        prefixGcd.sort()

        total_sum = 0
        l, r = 0, n - 1  

        while l < r:
            total_sum += math.gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1
        return total_sum