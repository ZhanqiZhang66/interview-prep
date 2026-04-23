class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1
        

    def count(self, point: List[int]) -> int:
        cnt = 0
        xx, yy = point
        for x, y in self.points.keys():
            if (abs(x - xx) != abs(y - yy)) or x == xx or y == yy:
                continue
            cnt += self.points.get((x, yy), 0) * self.points.get((xx, y), 0) * self.points[(x, y)]
        return cnt
   

        
        
