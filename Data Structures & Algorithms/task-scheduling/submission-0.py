class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = -1
            else:
                freq[task] -= 1
        heap = [cnt for cnt in freq.values()]
        heapq.heapify(heap)

        cycles = 0
        q = deque() # [-cnt, idletime]
        while heap or q:
            cycles += 1
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    q.append([cnt, cycles + n])
            if q and q[0][1] == cycles:
                heapq.heappush(heap, q.popleft()[0])
        return cycles

        