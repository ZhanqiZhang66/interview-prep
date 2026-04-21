class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if len(edges) != n - 1:
        #     return False
        # adj = [[] for _ in range(n)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)

        # seen = set()
        # def dfs(node):
        #     nonlocal seen
        #     seen.add(node)
        #     for nei in adj[node]:
        #         if nei not in seen:
        #             dfs(nei)

        
        # dfs(0)
        # return len(seen) == n
        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.size = [1] * n
            def find(self, node):
                if self.parent[node] == node:
                    return node
                return self.find(self.parent[node])
            def union(self, node1, node2):
                p1 = self.find(node1)
                p2 = self.find(node2)

                if p1 == p2:
                    return False
                if self.size[p2] > self.size[p1]:
                    p1, p2 = p2, p1 # p1 bigger
                self.size[p1] += self.size[p2]
                self.parent[p2] = p1
                return True
        if len(edges) != n - 1:
            return False
        uf = UnionFind(n)

        for u, v in edges:
            if uf.union(u, v) == False:
                return False
        return True
