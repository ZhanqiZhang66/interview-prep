class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        unique = {}
        for r in range(len(s)):
            curr_char = s[r]
            if curr_char in unique.keys():
                # l can only move forward
                l = max(l, unique[curr_char] + 1)       
            unique[curr_char] = r
            res = max(res, r - l + 1)     
        return res


        