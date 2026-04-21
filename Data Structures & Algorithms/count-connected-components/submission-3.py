class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u) 


        visited = [False] * n
        def dfs(node):
            nonlocal visited, adj
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)
        comp = 0
        for node in range(n):
            if not visited[node]:
                dfs(node)
                comp += 1
        return comp
        
        # class UnionFind:
        #     def __init__(self, n):
        #         self.parent = list(range(n))
        #         self.size = [1] * n
        #         self.components = n
        #     def find(self, node):
        #         if self.parent[node] == node:
        #             return node
        #         return self.find(self.parent[node])
        #     def union(self, node1, node2):
        #         root1 = self.find(node1)
        #         root2 = self.find(node2)
                
        #         if self.size[root1] > self.size[root1]:
        #             root1, root2 = root2, root1 # p1 is larger
        #         self.size[root1] += self.size[root2]
        #         self.parent[root2] = root1
        #         self.components -= 1
        
        # uf = UnionFind(n)
        # for u, v in edges:
        #     if uf.find(u) != uf.find(v):
        #         uf.union(u, v)
        # return uf.components
            

                
        