class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        from math import sqrt
        def dist(point):
            x, y = point[0], point[1]
            return sqrt(x**2 + y**2)
        minheap = []
        for point in points:
            minheap.append([dist(point), point[0], point[1]])
        heapq.heapify(minheap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minheap)
            res.append([x, y])
            k -= 1
        
        return res

            