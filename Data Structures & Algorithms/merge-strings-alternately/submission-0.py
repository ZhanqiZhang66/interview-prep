class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1, word2 = list(word1), list(word2)
        res = ""
        while word1 and word2:
            res += word1[0]
            res += word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        if word1:
            res += "".join(word1)
        if word2:
            res += "".join(word2)
        return res
        