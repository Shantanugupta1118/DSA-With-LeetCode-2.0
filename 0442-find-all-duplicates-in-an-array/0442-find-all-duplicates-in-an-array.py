class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n <= 1:
            return []

        hashMap = [0]*(n+1)
        dup = []
        for i in nums:
            if hashMap[i]:
                dup.append(i)
            hashMap[i] = 1
        return dup