class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        left = 0
        right = len(heights) - 1
        left_max = heights[0]
        right_max = heights[-1]
        ans = 0
        while left < right:
            width = right - left
            if heights[left] > left_max:
                left_max = heights[left]
            if heights[right] > right_max:
                right_max = heights[right]
            curr_contains = min(left_max, right_max) * width
            if curr_contains > ans:
                ans = curr_contains
                if left_max > right_max:
                    right -= 1
                else:
                    left += 1
            else:
                left += 1
                right -= 1
        return ans
        
        