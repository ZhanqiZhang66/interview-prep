class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        s1_counter = {}
        for s in s1:
            s1_counter[s] = s1_counter.get(s, 0) + 1
        l = 0
        s2_counter = {}
        for r in range(len(s2)):

            s2_counter[s2[r]] = s2_counter.get(s2[r], 0) + 1
            print(f"added {s2[r]} and count is {s2_counter.get(s2[r], 0)} in {s2_counter}")
            print(f"checking with {s1_counter} == {s2_counter} ")
   
            if (r - l + 1) > len(s1):

                print(f"remove {s2[l]} from {s2_counter}")
                s2_counter[s2[l]] -= 1
                if s2_counter[s2[l]] == 0:
                    del s2_counter[s2[l]]
                l += 1
            if s2_counter == s1_counter:
                return True
        return False
                
            

        