class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        total_rain = 0
        for i, h in enumerate(height):
            left_max = height[0]
            right_max = height[-1]
            if i == 0 or i == len(height) - 1:
                curr_rain = 0
                print(f"at {h}, get {total_rain} ")
            else:
                left = 0
                right = len(height) - 1
                while left < right:
                    if height[left] > left_max and left < i:
                        left_max = height[left]
                    if height[right] > right_max and right > i:
                        right_max = height[right]
                    right -= 1
                    left += 1
                lower_boarder = min(left_max, right_max)
                if lower_boarder > h:
                    curr_rain = lower_boarder - h
                else:
                    curr_rain = 0
                print(f"at {h}, get {total_rain} with left max {left_max} and right max {right_max}")
                
            total_rain += curr_rain
            
        return total_rain

            