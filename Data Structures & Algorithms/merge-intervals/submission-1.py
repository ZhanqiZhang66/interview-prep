class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        output = [intervals[0]]
        for start, end in intervals:
            stack_start, stack_end = output[-1]

            if start <= stack_end:
                output[-1][1] = max(stack_end, end)
            else:
                output.append([start, end])
        return output



        