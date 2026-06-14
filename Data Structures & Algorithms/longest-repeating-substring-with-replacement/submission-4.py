class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # maintain a sliding window
        counter = {}
        l = res = 0
        max_freq = 0

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            # s.t. k replacement in the window
            # most freq
            max_freq = max(max_freq, counter[s[r]])

            while (r - l + 1 - max_freq) > k :
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        # if there is more than k , _> shink the window from the left
        # otherwise move r pointer
        return res

        