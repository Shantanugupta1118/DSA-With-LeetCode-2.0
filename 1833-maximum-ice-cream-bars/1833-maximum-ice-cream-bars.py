class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        total = 0
        newcosts = sorted(costs)

        for i in newcosts:
            if total+i <= coins:
                total += i
                count += 1
            elif total+i > coins:
                break
        return count