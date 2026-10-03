class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        i = 0
        while i<len(nums):
            correctIdx = nums[i]-1
            if(nums[i] != nums[correctIdx]):
                nums[i], nums[correctIdx] = nums[correctIdx], nums[i]
            else:
                i+=1
        
        for i in range(len(nums)):
            if (nums[i] != i+1):
                return [nums[i], i+1]
        
