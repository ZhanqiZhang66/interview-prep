class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find the first idx such that > next idx
        # find peak, then on each side, call this
        n = mountainArr.length() - 1
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                r = mid 
            else:
                l = mid + 1
        peak_idx = l
        def binary_search(l, r, target, increase):
            while l <= r:
                mid = (r + l) // 2
                mid_val = mountainArr.get(mid)
                if mid_val == target:
                    return mid
                if increase:
                    if mid_val > target:
                        r = mid - 1
                    else:
                        l = mid + 1 
                else:
                    if mid_val > target:
                        l = mid + 1
                    else:
                        r = mid - 1 
            return -1
        i = binary_search(0, peak_idx, target, True)
        if i != -1:
            return i
        j = binary_search(peak_idx+1, n, target, False)
        if j != -1:
            return j
        return -1

        

        


        