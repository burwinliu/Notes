def grayCode(n: int):
    res = [0]
    def helper(r):
        print(r)
        if len(r) == 0:
                delta = abs(res[0] - res[-1])
            for i in n:
                if 2**i == delta:
                    return True
            return False
        for i in n:
            target = 2**i
            if res[-1] + target in r:
                res.append(res[-1] + target)
                r.remove(res[-1] + target)
                if helper(r):
                    return True
                r.add(res[-1] + target)
                res = res[:-1]
            if res[-1] - target in r:
                res.append(res[-1] - target)
                r.remove(res[-1] - target)
                if helper(r):
                    return True
                r.add(res[-1] - target)
                res = res[:-1]
        return False
    helper(set([i for i in range(1, 2**n)]))
    return res