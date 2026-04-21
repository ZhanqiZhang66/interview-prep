class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1*s for s in stones]
        while len(max_heap) > 1:
            heapq.heapify(max_heap)
            y = -1 * heapq.heappop(max_heap)
            x = -1 * max_heap[0]
            if x == y:
                pop = heapq.heappop(max_heap)
            if x < y:
                pop = heapq.heappop(max_heap)
                heapq.heappush(max_heap, -1 * (y - x) )
        return max_heap[0] * -1 if len(max_heap) else 0 
        