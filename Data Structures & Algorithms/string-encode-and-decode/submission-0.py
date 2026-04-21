class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            len_s = str(len(s))
            res += len_s
            res += s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        if s == "0":
            return [""]
        res = []
        len_s = ""
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                len_s += c
                i += 1
            else:
                w = s[i:i + int(len_s)]
                res.append(w)
                i += int(len_s)
                len_s = ""
        print("decode")
        print(res)
        return res

