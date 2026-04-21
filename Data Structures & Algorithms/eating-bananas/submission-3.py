class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        

        while left < right:
            mid = (left + right) // 2
            total_hour = sum([ (p + mid - 1) // mid for p in piles])
            if total_hour <= h:
                print(f"l={left} r={right}, mid={mid} {h} <= {total_hour}")
                right = mid
            else:
                print(f"l={left} r={right}, mid={mid} {h} > {total_hour}")
                left = mid + 1
        return left
            
        