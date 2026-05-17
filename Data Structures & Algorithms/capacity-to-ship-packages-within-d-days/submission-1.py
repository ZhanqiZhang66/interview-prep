class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # find first mid s.t -> count =  sum( sum(weights) < cap ) <= days
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            summ = 0
            count = 1
            # print(mid)
            for weight in weights:
                if summ + weight <= mid:
                    summ += weight
                    # print(f"count:{count}: weight {weight} added to {summ}")
                else:
                    summ = weight
                    count += 1
                    # print(f"new count:{count}: weight {weight} added to {summ}")
            if count <= days:
                r = mid
            else:
                l = mid + 1
        return l
            
        