class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1*s for s in stones]
        while len(max_heap) > 1:
            heapq.heapify(max_heap)
            print(max_heap)
            y = -1 * heapq.heappop(max_heap)
            x = -1 * max_heap[0]
            print(f"x={x}, y={y}")
            if x == y:
                pop = heapq.heappop(max_heap)
                print(f"remove both y={-1 * pop} and x={x},max_heap={max_heap}")
            if x < y:
                pop = heapq.heappop(max_heap)
                print(f"remove {-1 * pop}")
                heapq.heappush(max_heap, -1 * (y - x) )
                print(f"add {-1 * (y - x) }, max_heap={max_heap}")
        return max_heap[0] * -1 if len(max_heap) else 0 
        