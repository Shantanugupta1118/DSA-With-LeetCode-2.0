class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openStacks = []
        closeStacks = []

        for c in s:
            if c == '(':
                openStacks.append('(')
            elif c == ')' and len(openStacks) > 0:
                openStacks.pop()
            else:
                closeStacks.append(')')
        
        return len(openStacks) + len(closeStacks)