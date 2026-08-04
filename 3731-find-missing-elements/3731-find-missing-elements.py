class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        min_n = min(nums)
        max_n = max(nums)

        for i in range(min_n, max_n):
            if i not in nums:
                res.append(i)
        return res
