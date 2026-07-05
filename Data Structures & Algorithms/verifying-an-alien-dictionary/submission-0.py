class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {char:i for i, char in enumerate(order)}
 

        for j in range(1, len(words)):
            for i in range(len(words[j-1])):
                if i == len(words[j]):
                    return False
                if words[j-1][i] != words[j][i]:
                    if d[words[j-1][i]] > d[words[j][i]]:
                        return False
                    break
        return True


        