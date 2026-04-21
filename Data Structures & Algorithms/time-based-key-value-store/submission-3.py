class TimeMap:

    def __init__(self):
        self.map = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])    


        

    def get(self, key: str, timestamp: int) -> str:
        mood, values = "", self.map.get(key, [])
        l, r = 0, len(values)
        while l < r:
            mid = (l + r) // 2
            if values[mid][1] > timestamp:
                r = mid
            else:
                l = mid + 1
        if l - 1 >= 0:
            return values[l-1][0]
        else:
            return None
        
