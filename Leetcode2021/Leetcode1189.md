# Leetcode1189


```
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        record = {}
        numCount = {}
        for i in "balloon":
            record[i] = 0
            if i not in numCount:
                numCount[i] = 0
            numCount[i] += 1
        for i in text:
            if i in record:
                record[i] += 1
        res = float('inf')
        for i, j in record.items():
            res = min(res, j // numCount[i])
        return res
                
            
```