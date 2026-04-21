class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mono_increasing_heights = []
        max_area = 0
        # we append a sentinel 0:
        for i in range(len(heights)+1):
            while mono_increasing_heights and (i == len(heights) or heights[i] <= heights[mono_increasing_heights[-1]]):
                h = heights[mono_increasing_heights.pop()]
                w = i if not mono_increasing_heights else (i -1)- (mono_increasing_heights[-1] +1) + 1
                max_area = max(max_area, h * w)
            mono_increasing_heights.append(i)
        return max_area

#         Because the stack logic is:

# push until condition breaks
# then pop

# If the condition never breaks, the stack never empties.

# Sentinel ensures:

# condition breaks at the end


        