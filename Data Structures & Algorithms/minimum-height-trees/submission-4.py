class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n== 1:
            return [0]
        adj = defaultdict(set)
        for i in range(len(edges)):
            x, y = edges[i]
            adj[x].add(y)
            adj[y].add(x)
      
        queue = deque()
        indegrees = {}
        for node in adj:
            indegrees[node] = len(adj[node])
            if len(adj[node]) == 1:
                queue.append(node)
        while queue:
            if n <= 2:
                return list(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                n -= 1
                for nei in adj[node]:
                    indegrees[nei]  -= 1
                    if indegrees[nei] == 1:
                        queue.append(nei)



        