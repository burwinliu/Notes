# Leetcode926
Classic Prefix sum question. TOok a bit to figure it out, but this is the first one in some time to solve wihthout needing to spam results. there is a better solution w/ DP. Alt, don't store, and just as you go hold a count, and number of 1s to flip from prior, and min that with tentative results.


```
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count = [0, 0]
        record = []
        for i in s:
            record.append([count[0], count[1]])
            if i == '0':
                count[0] += 1
            elif i == '1':
                count[1] += 1
        record.append(count)
        numFlip = float('inf')
        for i in record:
            numFlip = min(numFlip, (count[0] - i[0]) + i[1])

        return numFlip
```
        