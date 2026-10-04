class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        n = len(nums)
        leftSum = 0
        rightSum = sum(nums)

        for i in range(len(nums)):
            if leftSum == (rightSum - leftSum - nums[i]):
                return i
            leftSum += nums[i]
        return -1