class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        def dfs(root, visited):
            if root == None:
                return -1
            if root in visited:
                return -1
            visited.add(root)
            h = []
            for nei in adj[root]:
                h.append(dfs(nei, visited))
            return max(h) + 1 

        adj = defaultdict(set)
        for i in range(len(edges)):
            x, y = edges[i]
            adj[x].add(y)
            adj[x].add(None)
            adj[y].add(x)
            adj[y].add(None)
      

        minh = float('inf')
        res = {}
        for node in range(n):
            h = dfs(node, set())
            res[node] = h

        ress = []
        for k, v in res.items():
            if v == min(res.values()):
                ress.append(k)
        return ress

        