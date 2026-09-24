class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = str(nums[i])
            tempSum = 0
            for x in temp:
                tempSum += int(x)
            if tempSum == i:
                return i
            
        return -1