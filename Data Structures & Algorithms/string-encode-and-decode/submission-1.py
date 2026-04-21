class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            len_s = str(len(s)) + "|"
            res += len_s
            res += s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        len_s = ""
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                len_s += c
                print(len_s)
                i += 1
            elif c == "|":
                i += 1
                if int(len_s) == 0:
                    w = ""
                    res.append(w)
                else:
                    w = s[i:i + int(len_s)]
                    res.append(w)
                    i += int(len_s)
                    len_s = ""
        # print("decode")
        # print(res)
        return res

