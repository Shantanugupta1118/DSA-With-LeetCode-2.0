class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for node_a, node_b, dist in roads:
            graph[node_a].append((node_b, dist))
            graph[node_b].append((node_a, dist))
        
        visited = [False]*(n+1)
        min_score = float('inf')

        def dfs(current_node):
            nonlocal min_score
            for nei, edge in graph[current_node]:
                min_score = min(min_score, edge)
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        visited[1] = True
        dfs(1)
        return min_score