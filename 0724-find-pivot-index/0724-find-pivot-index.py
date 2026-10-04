class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        leftSum = 0
        rightSum = sum(nums)

        for i in range(n):
            rightSum -= nums[i]
            if rightSum == leftSum:
                return i
            leftSum += nums[i]
            print("LeftSum: {}, RightSum: {}, Nums[i]: {}".format(leftSum, rightSum, nums[i]))
        return -1