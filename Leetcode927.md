# Leetcode927

Thinking goes -- if there are 3 equivalent sections, then there must be a divisible number of ones, with a pattern that repeats. Find that number of ones, find the corresponding pattern ( from the back ) and then search for the substring twice. if it occurs, you have match, else fail.

```
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        count = 0
        for i in arr:
            if i == 1:
                count += 1
        if count == 0:
            return [0, len(arr)-1]
        if count // 3 != count / 3:
            return [-1, -1]
        
        numOnes = count//3
        pos = -1
        record = []
        for i in range(numOnes):
            while arr[pos] != 1:
                record.append(0)
                pos -= 1
            record.append(1)
            pos -=1
        record = record[::-1]
        
        point = -1 
        res = []
        for i, j in enumerate(arr):
            if point == -1:
                if j == 1:
                    point = 0
                else:
                    continue
            
            if j != record[point]:
                return [-1, -1]
            point += 1
            if point == len(record):
                point = -1
                if len(res) == 0:
                    res.append(i)
                else:
                    res.append(i+1)
                    return res
            
            
            
        return [-1, -1]
```