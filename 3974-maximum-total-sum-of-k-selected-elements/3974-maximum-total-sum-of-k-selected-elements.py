class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)

        sublist = nums[:k]
        total = 0
        for i in sublist:
            total += i*mul
            if mul > 1:
                mul -= 1
        return total