class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        mxTotal = 0
        for i in accounts:
            mxTotal = max(mxTotal, sum(i))
        return mxTotal