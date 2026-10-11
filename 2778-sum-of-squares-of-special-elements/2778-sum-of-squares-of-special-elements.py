class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        totalSum = 0
        n = len(nums)
        for i in range(n):
            if n%(i+1) == 0:
                print("i: {}, sq_n: {}".format(i+1, nums[i]*nums[i]))
                totalSum += nums[i]*nums[i]
        return totalSum