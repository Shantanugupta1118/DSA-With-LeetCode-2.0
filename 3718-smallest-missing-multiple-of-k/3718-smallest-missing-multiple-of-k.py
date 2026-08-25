class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mul = [x*k for x in range(1,n+1)]

        for i in mul:
            if i not in nums:
                return i
        return k*(n+1)