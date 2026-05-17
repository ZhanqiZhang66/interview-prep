class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 2:
            return x
        l, r = 1, x
        # find first mid s.t mid **2 >= x
        while l < r:
            mid  = (l + r) // 2
            if mid * mid > x:
                r = mid
            else:
                l = mid + 1
        return l - 1 