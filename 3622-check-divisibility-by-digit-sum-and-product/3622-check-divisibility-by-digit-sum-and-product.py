class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1
        
        for digit in str(n):
            d = int(digit)
            digit_sum += d
            digit_prod *= d
            
        total_sum = digit_sum + digit_prod
        
        return n % total_sum == 0