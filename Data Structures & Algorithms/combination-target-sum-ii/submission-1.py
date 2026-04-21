class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(start, cur, com):
            if com == target:
                ans.append(cur.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue # tree branch of candidate[i] and candiditon[i-1] are the same
                if com + candidates[i] > target:
                    break
                cur.append(candidates[i])
                backtrack(i+1, cur, com + candidates[i])
                cur.pop()
        
        backtrack(0, [], 0)
        return ans
        