class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        m = abs(n)
        res = x
        while m > 1:
            res *= x
            m -= 1
        if n < 0:
            res = 1 / res
        return res