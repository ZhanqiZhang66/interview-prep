class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                j, prev_h = stack.pop()
                res = max(res, prev_h * (i - j))
                start = j
            stack.append((start, h))
        for k, h in stack:
            res = max(res, h* (len(heights) - k))
        return res

        