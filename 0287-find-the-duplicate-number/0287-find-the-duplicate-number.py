class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hashMap = {}
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        for i in range(len(nums)):
            if hashMap[nums[i]] > 1:
                return nums[i]