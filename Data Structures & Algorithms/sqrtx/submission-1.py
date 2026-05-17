class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0

        l, r = 1, x
        # find first mid s.t mid **2 >= x
        while l < r:
            mid  = (l + r) // 2
            if mid ** 2 > x:
                r = mid
            else:
                l = mid + 1
        return l - 1 if l > 1 else 1