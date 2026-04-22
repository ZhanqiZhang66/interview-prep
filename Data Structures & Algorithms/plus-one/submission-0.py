class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join(str(d) for d in digits)
        res = str(int(s) + 1)
        ans = []
        for r in res:
            ans.append(r)
        return ans

        