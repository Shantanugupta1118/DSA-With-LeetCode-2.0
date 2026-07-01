class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def in_bounds(r, c):
            return min(r,c) >= 0 and max(r,c)<n

        def pre_computing():
            queue = deque()
            mindist = {}
            for r in range(n):
                for c in range(n):
                    if grid[r][c]:
                        queue.append([r, c, 0])
                        mindist[(r,c)]=0
            while queue:
                r,c,dist = queue.popleft()
                neighbor = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]

                for r2, c2 in neighbor:
                    if in_bounds(r2, c2) and (r2, c2) not in mindist:
                        mindist[(r2, c2)] = dist+1
                        queue.append([r2, c2, dist+1])

            return mindist
        min_dist = pre_computing()
        maxHeap = [(-min_dist[(0,0)], 0, 0)]
        visit = set()
        visit.add((0,0))

        while maxHeap:
            dist, r, c = heapq.heappop(maxHeap)
            dist = -dist
            if (r,c) == (n-1, n-1):
                return dist
            neighbor = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for r2, c2 in neighbor:
                if in_bounds(r2, c2) and (r2, c2) not in visit:
                    visit.add((r2, c2))
                    dist2 = min(dist, min_dist[(r2, c2)])
                    heapq.heappush(maxHeap, (-dist2, r2, c2))
