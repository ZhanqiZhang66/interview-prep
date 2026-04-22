class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        while n not in visited:
            visited.add(n)
            s = 0
            for digit in str(n):
                s += int(digit) ** 2
            n = s
            if n == 1:
                return True
        return False

        