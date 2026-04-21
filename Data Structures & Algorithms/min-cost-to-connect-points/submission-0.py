class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        V = len(points)
        E = V - 1
        edges = []

        for x1, y1 in points:
            for x2, y2 in points:
                if x2 != x1 and y2 != y1:
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    if (dist, x1, y1, x2, y2) and (dist, x2, y2, x1, y1) not in edges:
                        edges.append((dist, x1, y1, x2, y2))
        edges.sort()

        class UnionFind:
            def __init__(self, points):
                self.parent = {(x, y): (x, y) for (x, y) in points}
                self.size = [1] * len(points)
            def find(self, node):
                if self.parent[node] != node:
                    return self.find(self.parent[node])
                else:
                    return node
            def union(self, n1, n2):
                r1, r2 = self.find(n1) , self.find(n2)

                if self.size[r2] > self.size[r1]:
                    r1, r2 = r2, r1
                self.size[r1] += self.size[r2]
                self.parent[r2] = r1
        

        uf = UnionFind(points)
        n = 0
        res = 0
        for dist, x1, y1, x2, y2 in edges:
            if uf.find((x1, y1)) != uf.find((x2, y2)):
                res += dist
                print(f'added ({x1},{y1} - {x2},{y2}) ={dist}')
                n+= 1
            if n == E:
                return res
        return -1


        

