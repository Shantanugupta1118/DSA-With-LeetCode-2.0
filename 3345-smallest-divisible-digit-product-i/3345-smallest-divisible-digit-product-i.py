class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def getDigitProduct(num):
            product = 1
            for d in str(num):
                product *= int(d)
            return product
        
        while getDigitProduct(n)%t != 0:
            n += 1
        
        return n