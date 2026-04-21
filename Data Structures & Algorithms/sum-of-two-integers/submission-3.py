class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0

        for i in range(32):
            a_bit = 1 & (a >> i) 
            b_bit = 1 & (b >> i) 
            summ = a_bit ^ b_bit ^ carry
            if summ:
                res = res | (summ << i)
            carry = 1 if a_bit & b_bit or a_bit & carry or b_bit & carry else 0
      
        mask = 0xFFFFFFFF
        if res >= 2**31:
            res -= 2**32
        return res 
        