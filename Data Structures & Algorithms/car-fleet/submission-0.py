class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(target - p, s) for p, s in zip(position, speed)]
        pair.sort()

        stack = []
        for dist, speed in pair:
            stack.append(dist/speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        