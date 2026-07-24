class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        leftmax, rightmax = height[l], height[r]
        while l < r:
            if leftmax < rightmax:
                res += leftmax - height[l]
                l += 1
                leftmax = max(leftmax, height[l])
                 
            else:
                res += rightmax - height[r]
                r -= 1
                rightmax = max(rightmax, height[r])
                
        return res
        