# Leetcode205
There is a more optimal solution with direct mapping (record, mapping s->t, check if match) but this was my initial solution. At any rate, O(N) time, O(1) space

```
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        records = dict()
        recordt = dict()
        pS = 0
        pT = 0
        for i in range(len(s)):
            curS = None
            curT = None
            if s[i] in records:
                curS = records[s[i]]
            else:
                curS = pS
                records[s[i]] = pS
                pS += 1
            if t[i] in recordt:
                curT = recordt[t[i]]
            else:
                curT = pT
                recordt[t[i]] = pT
                pT += 1
            if curS == curT:
                continue
            else:
                return False
        return True
```