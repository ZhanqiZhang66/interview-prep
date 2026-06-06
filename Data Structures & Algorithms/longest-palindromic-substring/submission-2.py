class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)] # s[j: i] is palindrome
        s_i = 0
        s_j = 0
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j]:
                    if i - j <= 2 or dp[j+1][i-1] :
                        dp[j][i] = True
                        if (i - j) > (s_i - s_j):
                            s_i = i
                            s_j = j
        return s[s_j: s_i+1]

        