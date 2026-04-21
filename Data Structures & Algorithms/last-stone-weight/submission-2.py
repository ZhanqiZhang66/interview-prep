class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1*s for s in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            y = -1 * heapq.heappop(max_heap)
            x = -1 * heapq.heappop(max_heap)
            if x < y:
                heapq.heappush(max_heap, -1 * (y - x) )
        return abs(max_heap[0]) if len(max_heap) else 0 
        