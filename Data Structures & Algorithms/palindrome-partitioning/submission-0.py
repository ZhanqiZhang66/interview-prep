class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s) - 1
        ans = []

        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l+= 1
                r -= 1
            return True

        # aab, aa b, a ab
        # a aab, aa ab, aaa b, aaab | []
                            # a |  aab,  a ab, aa b

        def backtrack(start, curr):
            # cut_i = 1 == before i==1, a|ab
            if start == len(s):
                ans.append(curr.copy())
                return 
        
            for j in range(start, len(s)):
                if isPalindrome(s[start:j+1]):      
                    curr.append(s[start:j+1])
                    backtrack(j+1, curr)
                    curr.pop()

        backtrack(0, [])
        return ans


        
        