class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # use a stack to store  record
        record = []
        for op in operations:
            if op.isdigit() or op[0] == "-":
                if op[0] == "-":
                    d = -1 * int(op[1:])
                else:
                    d = int(op)
                record.append(d)
            elif op == "+":
                if len(record) > 1:
                    record.append(record[-1] + record[-2])
            elif op == "C":
                if record:
                    record.pop()
            elif op == "D":
                if record:
                    record.append(record[-1] * 2)
        # return sum
        return sum(r for r in record)
        