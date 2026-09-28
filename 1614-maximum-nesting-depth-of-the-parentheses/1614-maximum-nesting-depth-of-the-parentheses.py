class Solution:
    def maxDepth(self, s: str) -> int:
        currDepth = 0
        maxDepth = 0

        for c in s:
            if c == '(':
                currDepth += 1
                maxDepth = max(maxDepth, currDepth)
            elif c == ')':
                currDepth -= 1
        return maxDepth