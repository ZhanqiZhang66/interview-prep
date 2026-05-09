class Solution:
    # For this question I like to think of the table being filled with water,
    # then the wind sweeping the water off from the left and then the right.
    def trap(self, height: List[int]) -> int:
        l = res = 0
        r = len(height) - 1
        lmax, rmax = height[0], height[-1]

        while l < r:
            if height[l] < height[r]:
                l += 1
                if height[l] <= lmax:
                    res += lmax - height[l]
                else:
                    lmax = height[l]
            else:
                r -= 1
                if height[r] <= rmax:
                    res += rmax - height[r]
                else:
                    rmax = height[r]
        return res