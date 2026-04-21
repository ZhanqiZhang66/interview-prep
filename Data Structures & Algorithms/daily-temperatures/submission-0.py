class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        cooler = deque()

        res = [0] * len(temperatures)
      
        for j, temp in enumerate(temperatures):
            while cooler and temp > cooler[-1][0]:
                # print(f"{temp} > {cooler[-1][0]} in {cooler}")
                temperature, i = cooler.pop()
                res[i] = j - i 
                # print(res)
            cooler.append(((temp, j)))
        return res
            
