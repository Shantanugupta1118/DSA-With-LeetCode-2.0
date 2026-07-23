class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return n
        bit_length = n.bit_length()
        return 1<<bit_length