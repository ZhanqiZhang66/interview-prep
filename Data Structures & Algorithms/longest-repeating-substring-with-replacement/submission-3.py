class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        counter = {}
        l = 0
        ans = 0
        max_freq = 0
        for r in range(len(s)):
            if s[r] not in counter.keys():
                counter[s[r]] = 1
            else:
                counter[s[r]] += 1
            # counter[s[r]] = 1 + counter.get(s[r], 0)
            max_freq = max(max_freq, counter[s[r]])
            while (r - l + 1) - max_freq > k:
                counter[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans



        


        