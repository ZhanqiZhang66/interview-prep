class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.size = [1] * n
            def find(self, node):
                if self.parent[node] != node:
                    return self.find(self.parent[node])
                return node
            def union(self, node1, node2):
                r1 = self.find(node1)
                r2 = self.find(node2)

                if self.size[r1] < self.size[r2]:
                    r1, r2 = r2, r1
                self.size[r1] += self.size[r2]
                self.parent[r2] = r1
        
        n = len(edges) +1
        uf = UnionFind(n)
        for u, v in edges:
            if uf.find(u) == uf.find(v):
                return [u, v]
            uf.union(u, v)
        return []




        # n = len(edges)
        # adj = [[] for _ in range(n+1)]

        # def dfs(u, par):
        #     nonlocal visited
        #     if visited[u]:
        #         return True

        #     visited[u] = True
        #     for nei in adj[u]:
        #         if nei == par:
        #             continue
        #         if dfs(nei, u):
        #             return True
        #     return False
              
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        #     visited = [False] * (n+1)

        #     if dfs(u, -1):
        #         return [u, v]


        # return []


        