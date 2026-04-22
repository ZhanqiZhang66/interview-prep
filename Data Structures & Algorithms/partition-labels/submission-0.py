class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        from collections import Counter
        counter = Counter(s)
        print(counter)
        res = []
        tmp = []
        for j, ch in enumerate(s):
            tmp.append(ch)
            counter[ch] -= 1
            print(f"{ch} - count:{counter[ch]} - {tmp}")
            i = 0
            for t in set(tmp):
                if counter[t] == 0:
                    i += 1
                    print(f"i={i}")
                    if i == len(set(tmp)):
                        print(f"i = {i} and {tmp}")
                        res.append(len(tmp))
                        tmp = []
        return res

      
                
            
         