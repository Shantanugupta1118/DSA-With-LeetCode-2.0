class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        coveredCount = 0
        maxEndPoint = -inf

        for i, j in intervals:
            if j > maxEndPoint:
                coveredCount += 1
                maxEndPoint = j
        return coveredCount