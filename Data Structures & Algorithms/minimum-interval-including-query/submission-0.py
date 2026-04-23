class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sweep = {}
        length = defaultdict(list)
        for start, end in intervals:
            for i in range(start, end + 1):
                length[i].append(end - start + 1)
                # length[end].append(end - start + 1)
            # sweep[start] += 1
            # sweep[end] -= 1
        print(length)
        res = []
    
        for t in queries:
            if t in length:
                print(f"at {t} {length[t]}")
                res.append(min(length[t]))
            else:
                res.append(-1)
        return res


        