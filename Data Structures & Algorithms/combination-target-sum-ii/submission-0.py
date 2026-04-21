class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(start, cur, com):
            if com == target and cur not in ans:
                ans.append(cur.copy())
                return
            
            for i in range(start, len(candidates)):
                if com + candidates[i] > target:
                    continue
                cur.append(candidates[i])
                backtrack(i+1, cur, com + candidates[i])
                cur.pop()
        
        backtrack(0, [], 0)
        return ans
        