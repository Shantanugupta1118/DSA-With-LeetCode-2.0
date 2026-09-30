class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        maxDepth = []
        depth = 0

        for char in seq:
            if char == '(':
                depth += 1
                maxDepth.append(depth%2)
            else:
                maxDepth.append(depth%2)
                depth -= 1
        return maxDepth
