class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        from collections import Counter
        mp = {}
        for i, ch in enumerate(s):
            mp[ch] = i
        
        end = 0
        size = 0
        res = []
        for i, c in enumerate(s):
            end = max(end, mp[c])
            size += 1
            if end == i:
                res.append(size)
                size = 0
        return res
                


      
                
            
         