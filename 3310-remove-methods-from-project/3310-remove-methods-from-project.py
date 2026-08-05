class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)

        susp = set([k])
        queue = deque([k])

        while queue: 
            nd = queue.popleft()
            for nei in adj[nd]:
                if nei not in susp:
                    susp.add(nei)
                    queue.append(nei)

        for u, v in invocations:
            if u not in susp and v in susp:
                return list(range(n))

        return [i for i in range(n) if i not in susp]