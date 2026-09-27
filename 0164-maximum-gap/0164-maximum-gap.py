class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) <=1:
            return 0

        diff_check = -1
        nums.sort()
        for i in range(len(nums)-1):
            diff_check = max(diff_check, nums[i+1]-nums[i])
        return diff_check