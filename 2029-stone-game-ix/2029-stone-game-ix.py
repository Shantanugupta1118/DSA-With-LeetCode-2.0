class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0]*3

        for i in stones:
            count[i%3]+=1
        return count[1]>=1 and count[2]>=1 if count[0]%2 == 0 else abs(count[1] - count[2]) > 2