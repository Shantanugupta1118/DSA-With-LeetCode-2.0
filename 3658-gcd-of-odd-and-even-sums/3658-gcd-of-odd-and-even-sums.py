class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd, even = 0, 0
        for i in range(n*2):
            if i%2==0:  #even
                even += i
            else:   #odd
                odd += i
        return math.gcd(odd, even)