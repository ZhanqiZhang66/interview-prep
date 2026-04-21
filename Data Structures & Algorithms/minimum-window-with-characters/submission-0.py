class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not s:
            return ""

        counter_t = {}
        for ch in t:
            counter_t[ch] = counter_t.get(ch, 0) + 1
        l = 0
        shortest = len(s)
        substring = shortest_substring = t
        counter_s = {}

        def contains_dict(counter_s, counter_t):
            for char in counter_t.keys():
                if char not in counter_s.keys():
                    # print(f"counter_t[{char}] != counter_s[{char}] {counter_t[char] != counter_s[char]}")
                    # print(f"{char} not in counter_s")
                    return False
                elif counter_s[char] < counter_t[char]:
                    return False
            return True

        for r in range(len(s)):
            counter_s[s[r]] = counter_s.get(s[r], 0) + 1
            # print(f"adding {s[r]} to {counter_s}")
            # print(f"checking {contains_dict(counter_s, counter_t)}")

            while contains_dict(counter_s, counter_t):
                substring = s[l:r+1]
                print(f"find {t} in {s} = {substring}")
                counter_s[s[l]] -= 1
                if counter_s[s[l]] == 0:
                    del counter_s[s[l]]
                l += 1
                # print(f"find {t} in {s} = {substring}\nl at {s[l]} removing {s[l]} and {counter_s}")
                if len(substring) < shortest:
                    shortest = len(substring)
                    shortest_substring = substring
                    print(f"shortest is {shortest_substring}")
        return shortest_substring

            

            


        

        