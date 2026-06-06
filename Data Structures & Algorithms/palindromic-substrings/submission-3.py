class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        num_palindrome = 0
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1):
                if s[j] == s[i] and ((i - j) <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    num_palindrome += 1
        return num_palindrome

        