import math
def grayCode(n: int):
    def helper(record, res):
        if len(record) == 0:
            if math.log2(abs(res[0] - res[-1]))%1 == 0:
                return res
            return None
        for i in range(n):
            checkShift = 2**i
            print(record, checkShift)
            if res[-1] + checkShift in record:
                record.remove(res[-1] + checkShift)
                res.append(res[-1] + checkShift)
                if helper(record, res):
                    return res
                print(res, record, "POS")
                res = res[:-1]
                record.add(res[-1] + checkShift)
                print(res, record)

            if res[-1] - checkShift in record:
                record.remove(res[-1] - checkShift)
                res.append(res[-1] - checkShift)
                if helper(record, res):
                    return res
                print(res, record, "NEG")
                res = res[:-1]
                record.add(res[-1] - checkShift)
                print(res, record)
    helper(set([i for i in range(1, 2**n)]), [0])
grayCode(2)