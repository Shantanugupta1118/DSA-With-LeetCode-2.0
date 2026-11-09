from heapq import heappop, heappush
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        busy = []  
        count = [0] * k

        for i, (a, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                _, server_id = heappop(busy)
                available.add(server_id)

            if not available:
                continue

            idx = available.bisect_left(i % k)
            if idx == len(available):
                idx = 0  
            
            server_id = available.pop(idx)
            count[server_id] += 1
            heappush(busy, (a + l, server_id))

        max_reqs = max(count)
        return [i for i, c in enumerate(count) if c == max_reqs]