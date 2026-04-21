class Solution:
    def getSum(self, a: int, b: int) -> int:
        a_bits = [1 & (a >> i) for i in range(32)][::-1]
        b_bits = [1 & (b >> i) for i in range(32)][::-1]

        carry = 0
        i = 0
        res = 0
        print(a_bits)
        print(b_bits)
        while a_bits and b_bits:
            aa = a_bits.pop()
            bb = b_bits.pop()
            summ = aa ^ bb ^ carry
            
            res += summ << i
            carry = 1 if aa & bb else 0
            i += 1
        return res
        