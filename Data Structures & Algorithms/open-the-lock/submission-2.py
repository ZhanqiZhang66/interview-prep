class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def adj(num):
            # print(num)
            nei = []
            for i in range(4):
                numi = int(num[i])
                p = (numi + 1) % 10
                c1 = num[:i] + str(p) + num[i+1:]
                m = (numi -1 + 10) % 10
                c2 = num[:i] + str(m) + num[i+1:]
                nei.append(c1)
                nei.append(c2)
            return nei
        if "0000" in deadends:
            return -1
        res = 0
        q = deque(["0000"])
        visited = set(deadends)
        while q:
            for _ in range(len(q)):
                num = q.popleft()
                if num == target:
                    return res

                for nei in adj(num):
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            res += 1
        return -1

        