class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        used = [] # used: end time and room num
        free = [i for i in range(n)] # free: room num
        cnt = [0] * n
        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(free, room)
            if not free:
                prev_end, room = heapq.heappop(used)
                end = prev_end + (end - start)
                heapq.heappush(free, room)
         
            room = heapq.heappop(free)
            heapq.heappush(used, (end, room))
     
            cnt[room] += 1
        return cnt.index(max(cnt))
            
                


        