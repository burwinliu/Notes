# Leetcode598 
A cute little problem. FIgure out that you can't move the origin of the operations, and the answer of minimize the size is clear as the result

```
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        curMin = [m, n]
        for i in ops:
            curMin = [min(i[0], curMin[0]), min(i[1], curMin[1])]
        return curMin[0] * curMin[1]
```

