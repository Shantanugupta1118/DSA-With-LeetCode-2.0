class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened = 0
        res= ''
        for c in s:
            if c == '(':
                if opened > 0:
                    res += c
                opened += 1
            elif c == ')':
                opened -= 1
                if opened > 0:
                    res += c
        return res 