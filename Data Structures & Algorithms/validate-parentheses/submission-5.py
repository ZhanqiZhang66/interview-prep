class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s)%2 == 1:
            return False
        valid_pairs = {"{":"}", "[":"]", "(":")"}
        q = deque()
        for p in s:
            if p in valid_pairs.keys():
                q.append(p)
            else:
                if q and valid_pairs[q[-1]] == p:
                    q.pop()
                else:
                    return False
        return len(q) == 0

        