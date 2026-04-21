class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(curr):    
            if sum(curr) == target:
                freq = {num: 0 for num in nums}
                for item in curr:
                    freq[item] += 1
                if freq not in res:
                    res.append(freq)
                    return
            for num in nums:
                if sum(curr) > target:
                    continue
                curr.append(num)
                backtrack(curr)
                curr.pop()
            return res

        backtrack([])
        res_l = []
        print(res)
        for freq in res:
            tmp = []
            for k, v in freq.items():
                tmp += [k]* v
            res_l.append(tmp)
            
        return res_l
        