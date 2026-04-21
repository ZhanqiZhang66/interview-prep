class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        valid_pairs = {"{":"}", "[":"]", "(":")"}
        q = deque()
        for p in s:
            if p in valid_pairs.keys():
                q.append(p)
            else:
                if valid_pairs[q[-1]] != p:
                    # print(f"{q[-1]} should pair with {valid_pairs[q[-1]]} and we have {p}")
                    # print(f"q = {q}")
                    return False
                else:
                    # print(f"{q[-1]} should pair with {valid_pairs[q[-1]]} and we have {p}")
                    # print(f"q = {q}")
                    q.pop()
                    # print(f"q = {q}")
                    continue
        return True

        