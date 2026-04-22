class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def mult(num1, num2, prev_carry):
            mul = int(num1) * int(num2) + prev_carry
            res = mul % 10
            carry = mul // 10
            return carry, res
        def ad(num1, num2, i):
            return num1 + num2 * (10 ** i)

        
        total = 0
        for j, digit2 in enumerate(num2[::-1]):
            res = 0
            prev_carry = 0
            for i, digit1 in enumerate(num1[::-1]):
                carry, mul = mult(digit2, digit1, prev_carry)
                res += mul * (10 ** i)
                prev_carry = carry
            if prev_carry:
                res += prev_carry * (10 ** (i+1))
            total = ad(total, res, j)
        return str(total)
            
        