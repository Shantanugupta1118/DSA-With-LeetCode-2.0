class Solution:
    def minSubArrayLen(self, target, nums):
        subArrayCount = float('inf')
        current_sum = 0
        l = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            while current_sum >= target:
                subArrayCount = min(subArrayCount, i-l+1)
                current_sum -= nums[l]
                l+=1
        return 0 if subArrayCount==float('inf') else subArrayCount