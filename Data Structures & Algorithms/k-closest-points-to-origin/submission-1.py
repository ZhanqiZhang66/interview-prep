class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            d = math.sqrt((x)**2 + (y)**2)
            heap.append((-d, x, y))
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        res = []
        while heap:
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res
        