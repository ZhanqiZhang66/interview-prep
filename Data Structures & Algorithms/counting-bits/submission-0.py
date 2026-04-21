class Solution:
    def countBits(self, n: int) -> List[int]:
        def countone(n):
            res = 0
            for i in range(32):
                if (1 << i) & n:
                    res += 1
            return res
        cnt = []
        for i in range(n + 1):
            cnt.append(countone(i))
        return cnt


        