class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # use a stack to store  record
        record = []
        res = 0
        for op in operations:
            if op == "+":
                if len(record) > 1:
                    res += record[-1] + record[-2]
                    record.append(record[-1] + record[-2])
                    
            elif op == "C":
                if record:
                    res -= record[-1]
                    record.pop()
                    
            elif op == "D":
                if record:
                    res += record[-1] * 2
                    record.append(record[-1] * 2)
                    
            else:
                res += int(op)
                record.append(int(op))
                
        # return sum
        return res
        