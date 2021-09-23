# Leetcode954
Counter and match off -- pretty standard.

An interesting variation is the idea that every item in position [i] -> [i\*2+1] s.t. 2*val[i] ==  val[i\*2+1]. Not sure how that would map out though..  Heap style solution probably?

For this problem, the important thing is that everyon maps to everyone, and that by sorting (with abs in mind) you can iterate upwards and find the proper match w/o issue.

```
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr = sorted(arr, key=abs)
        
        record = {}
        for i in arr:
            if i in record and record[i] > 0:
                record[i] -= 1
            else:
                if i*2 not in record:
                    record[i*2] = 0
                record[i*2] += 1
        return sum(record.values()) == 0
        
```