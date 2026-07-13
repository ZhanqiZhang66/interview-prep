 # UnionFind
class UnionFind:
    def __init__(self, n):
        # parent : what is the root of a node
        self.parent = list(range(n))
        # sizes of each components 
        self.sizes = [1] * n
    def find(self, x):
        
        # this node has a different node as parent
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        # this node is its own parent
        return self.parent[x]
    def union(self, x, y):
        # 1. root (x) == root(y)
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if rx != ry:
            if self.sizes[rx] < self.sizes[ry]:
                rx, ry = ry, rx
            # merge root(y ) into x
            self.parent[ry] = rx
            self.sizes[rx] += self.sizes[ry]
        return True
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
       
        c = n
        uf = UnionFind(n)
        for a, b in edges:
            if uf.union(a, b):
                c -= 1
        # for each node, union them if they are in the same graph, 
        return c 
        