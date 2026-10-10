class Solution:
    def mySqrt(self, x: int) -> int:
        high = x
        low = 1
        
        while low <= high:
            mid = (low+high)//2
            if mid*mid==x:
                return mid
            if (mid*mid) > x:
                high = mid - 1
            else:
                low = mid + 1 
        return high

        
