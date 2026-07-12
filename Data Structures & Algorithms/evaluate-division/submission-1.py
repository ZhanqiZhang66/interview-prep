class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        class UnionFind:
            def __init__(self):
                self.parent = {}
                self.weights = {}
            def add(self, node):
                if node not in self.parent:
                    self.parent[node] = node
                    self.weights[node] = 1
            def find(self, node):
                if self.parent[node] != node:
                    pre_par = self.parent[node]
                    self.parent[node] = self.find(self.parent[node])
                    self.weights[node] *= self.weights[pre_par] 
                return self.parent[node]
            def union(self, x, y, v):
                self.add(x)
                self.add(y)
                rx, ry = self.find(x), self.find(y)

                if rx != ry:
                    self.parent[rx] = ry
                    self.weights[rx] = self.weights[y] * v / self.weights[x]
            def get_ratio(self, x, y):
                if x not in self.parent or y not in self.parent or self.find(x) != self.find(y):
                    return -1
                if x == y:
                    return 1
                return self.weights[x] / self.weights[y]
        uf = UnionFind()
        for (x, y), v in zip(equations, values):
            uf.union(x, y, v)
        res = []
        for (x, y) in queries:
            res.append(uf.get_ratio(x, y))
        return res
            
