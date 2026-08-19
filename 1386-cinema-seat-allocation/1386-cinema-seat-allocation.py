from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_masks = defaultdict(int)
        for row, seat in reservedSeats:
            row_masks[row] |= (1 << (seat - 1))
            
        LEFT = 0b0111100000    # Seats 2, 3, 4, 5
        RIGHT = 0b0000011110   # Seats 6, 7, 8, 9
        MIDDLE = 0b0001111000  # Seats 4, 5, 6, 7
        
        ans = 0
        
        for mask in row_masks.values():
            left_free = (mask & LEFT) == 0
            right_free = (mask & RIGHT) == 0
            middle_free = (mask & MIDDLE) == 0
            
            if left_free and right_free:
                ans += 2
            elif left_free or right_free or middle_free:
                ans += 1
                
        empty_rows = n - len(row_masks)
        ans += empty_rows * 2
        
        return ans