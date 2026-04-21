class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        dp = [0] * n # maximum num of non overlapp
        dp[0] = 1

        for i in range(n):
            start, _ = intervals[i]
            dp[i] = 1
            for j in range(i):
                _, prev_end = intervals[j]
                if start >= prev_end:
                    dp[i] = max(dp[i], 1+ dp[j])
        return n - max(dp)


        # prev_end = intervals[0][1]
        # remove = 0

        # for start, end in intervals[1:]:
        #     if start < prev_end:
        #         prev_end = min(end, prev_end)
        #         remove += 1
        #     else:
        #         prev_end = end
        # return remove


        