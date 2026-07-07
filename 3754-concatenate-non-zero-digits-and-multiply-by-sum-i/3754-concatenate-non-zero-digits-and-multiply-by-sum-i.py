class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0: return 0
        res = ''
        mul = 0
        for i in str(n):
            if int(i) > 0:
                res += i
                mul += int(i)
        return int(res)*mul
