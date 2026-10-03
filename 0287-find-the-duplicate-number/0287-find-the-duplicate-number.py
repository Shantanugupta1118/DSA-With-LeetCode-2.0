class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hashMap = [0]*len(nums)
        for i in nums:
            if hashMap[i]:
                return i
            hashMap[i] = 1