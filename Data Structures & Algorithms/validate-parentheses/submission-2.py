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
                if q and valid_pairs[q[-1]] != p:
                    print(f"{q[-1]} should pair with {valid_pairs[q[-1]]} and we have {p}")
                    print(f"q = {q}")
                    return False

                else:
                    # print(f"{q[-1]} should pair with {valid_pairs[q[-1]]} and we have {p}")
                    # print(f"q = {q}")
                    if q:
                        q.pop()
                    else:
                        return False
                    # print(f"q = {q}")
                    # continue
        return True

        