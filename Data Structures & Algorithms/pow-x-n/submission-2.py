class Solution:
    def myPow(self, x: float, n: int) -> float:
        def poww(x, n):
            if n == 0:
                return 1
            if n % 2:
                return poww(x ** 2, n // 2) * x
            else:
                return poww(x ** 2, n // 2)
        res = poww(x, abs(n))
        return res if n >= 0 else 1 / res