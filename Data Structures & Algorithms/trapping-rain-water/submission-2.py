class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0
        left_max = height[0]
        right_max = height[-1]
        left, right = 0, len(height) - 1
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(height[left], left_max)
                res += left_max - height[left]
                
            else:
                right -= 1
                right_max = max(height[right], right_max)
                res += right_max - height[right]

      
            
        return res

            