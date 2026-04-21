class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        l = 0
        ans = []
        from collections import deque
        q = deque()

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                # print(f"{q[-1]} <  {nums[r]}")
                q.pop()
                # print(f"{q}")
            q.append(r)
            # print(f"{q}")
            while r - l + 1 > k:
                if q and q[0] == l:
                    q.popleft()
                    # print(f"{q}")
                l += 1
            if r - l + 1 == k:
                ans.append(nums[q[0]])
                # print(f"r={r}, {ans}")
        return ans

        