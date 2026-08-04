class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        min_n = inf
        max_n = -inf

        for i in nums:
            min_n = min(min_n, i)
            max_n = max(max_n, i)

        for i in range(min_n, max_n):
            if i not in nums:
                res.append(i)
        return res
