class Solution:
    def reverse(self, x: int) -> int:
        org = x
        x = abs(x)
        res = int(str(x)[::-1])
        if org < 0:
            res *= -1
        
        if res not in range(-2 ** 31, 2**31):
            return 0
        return res



        