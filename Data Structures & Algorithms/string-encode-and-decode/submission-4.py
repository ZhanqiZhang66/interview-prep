class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "|" + s 
        return res

    def decode(self, s: str) -> List[str]: 
        res = []
        count = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                count = int(c) + count * 10 
                i += 1
            elif c == "|":
                i += 1
                if count == 0:
                    res.append("")    
                else:
                    substr = s[i: i+count] 
                    i += count
                    res.append(substr)
                    count = 0
        return res

                
