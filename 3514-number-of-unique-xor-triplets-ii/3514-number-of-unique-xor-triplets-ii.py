class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        max_val = max(nums)
        limit = 1
        while limit <= max_val:
            limit <<= 1
            
        has_pair = [False] * limit
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                has_pair[nums[i] ^ nums[j]] = True
                
        has_triplet = [False] * limit
        for pair_xor in range(limit):
            if has_pair[pair_xor]:
                for num in nums:
                    has_triplet[pair_xor ^ num] = True
                    
        return sum(has_triplet)
