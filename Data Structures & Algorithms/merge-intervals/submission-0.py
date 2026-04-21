class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        prev_s, prev_e = intervals[0]
        for i in range(1, len(intervals)):
            cur_s, cur_e = intervals[i]
            if cur_s > prev_e:
                if [prev_s, prev_e] not in res:
                    res.append([prev_s, prev_e])
                    print(f"{cur_s} > {prev_e}, {prev_s} {prev_e} - {res}")
            elif cur_e < prev_s:
                if [prev_s, prev_e] not in res:
                    res.append([prev_s, prev_e])
                    print(f"{cur_e} < {prev_s}, {prev_s} {prev_e} - {res}")
            else:
                cur_s = min(cur_s, prev_s)
                cur_e = max(cur_e, prev_e)
                res.append([cur_s, cur_e])
                print(f"overlap {cur_s} {cur_e} - {res}")
            prev_s, prev_e = res[-1]
        if [cur_s, cur_e] not in res:
            res.append([cur_s, cur_e])
            print(f"add last {cur_s} {cur_e} - {res}")
        return res


        