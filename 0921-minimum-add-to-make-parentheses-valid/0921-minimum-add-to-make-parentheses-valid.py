class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openStacks = 0
        closeStacks = 0

        for c in s:
            if c == '(':
                openStacks += 1
            elif c == ')' and openStacks > 0:
                openStacks -= 1
            else:
                closeStacks += 1
        
        return openStacks + closeStacks