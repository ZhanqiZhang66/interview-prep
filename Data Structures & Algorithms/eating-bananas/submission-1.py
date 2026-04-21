class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = list(range(1, max(piles)+1))
        print(k)
        left = 0
        right = len(k) - 1
        

        while left < right:
            mid = (left + right) // 2
            total_hour = sum([ (p + k[mid] - 1) // k[mid] for p in piles])
            if total_hour <= h:
                print(f"l={left} r={right}, mid={k[mid]} {h} <= {total_hour}")
                right = mid
            else:
                print(f"l={left} r={right}, mid={k[mid]} {h} > {total_hour}")
                left = mid + 1
        return k[left]
            
        