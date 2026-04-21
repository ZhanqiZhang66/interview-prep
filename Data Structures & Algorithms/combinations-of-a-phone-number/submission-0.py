class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapper = {"2": "abc", 
                  "3": "def", 
                  "4":"ghi", 
                  "5":"jkl", 
                  "6":"mno", 
                  "7":"pqrs",
                  "8":"tuv", 
                  "9":"wxyz"}
        ans = []
        if len(digits) == 0:
            return []

        def backtrack(start, curr):
            if start == len(digits):
                ans.append("".join(curr))
                return

            letters = mapper[digits[start]] 
            for c in letters:
                curr.append(c)
                backtrack(start+1, curr)
                curr.pop()

        backtrack(0, [])
        return ans
        