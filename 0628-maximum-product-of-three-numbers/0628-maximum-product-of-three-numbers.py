class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        res1 = nums[0]*nums[1]*nums[-1]
        res2 = nums[-1]*nums[-2]*nums[-3]
        return max(res1, res2)
        