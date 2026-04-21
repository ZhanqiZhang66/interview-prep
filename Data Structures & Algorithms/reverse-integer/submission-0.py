class Solution:
    def reverse(self, x: int) -> int:
        i = 0
        digits = []
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        while x:
            digits.append(x % 10)
            x  = x // 10
            i += 1
        print(digits)
        res = 0
        i -= 1
        for digit in digits:
            res += digit * 10 ** i
            i -= 1
        res = res * sign
        return res if res in range(-2**31, 2**31) else 0


        