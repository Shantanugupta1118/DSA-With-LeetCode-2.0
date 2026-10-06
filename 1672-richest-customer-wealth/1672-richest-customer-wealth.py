class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(map(lambda x:sum(x), accounts))