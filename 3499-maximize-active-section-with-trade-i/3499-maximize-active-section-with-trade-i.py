class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        total_ones = s.count('1')
        
        max_gain = 0
        prev_zeros = 0
        curr_zeros = 0
        block_count = 0  # Track total number of independent '0' blocks
        
        for char in s:
            if char == '0':
                curr_zeros += 1
            else:
                if curr_zeros > 0:
                    block_count += 1
                    if block_count >= 2:
                        max_gain = max(max_gain, prev_zeros + curr_zeros)
                    prev_zeros = curr_zeros
                    curr_zeros = 0
                    
        if curr_zeros > 0:
            block_count += 1
            if block_count >= 2:
                max_gain = max(max_gain, prev_zeros + curr_zeros)
            
        # If there are fewer than 2 zero blocks, no trade is possible
        if block_count < 2:
            return total_ones
            
        return total_ones + max_gain
