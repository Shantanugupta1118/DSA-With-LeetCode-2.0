class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res = res + (ord('z') - ord(s[i]) + 1)*(i+1)
        return res