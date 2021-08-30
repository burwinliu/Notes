# Leetcode1235

This one is a real doozy.

See approach one (DP with O(n^2) time solution). TLEs, as n^2 is too slow. Idea is to check every possible future path that may be taken, and if it is more optimal, use that path. 

```
class Solution:        
    def jobScheduling(self, startTime, endTime, profit) -> int:
        
        # Construct the data structure for times
        record = []
        for i in range(len(startTime)):
            record.append((startTime[i], endTime[i], profit[i]))
        record = sorted(record, key=itemgetter(0,1))
        
        memo = [[profit[i] for _ in range(len(profit))] for i in range(len(profit))]
        
        for i in range(len(profit)):
            curIndex = -1 - i
            memo[curIndex][curIndex] = record[curIndex][2]
            curMax = record[curIndex][2]
            for j in range(len(profit) - i, len(profit)):  
                if record[j][0] < record[curIndex][1]:
                    memo[curIndex][j] = max(memo[curIndex][j-1], memo[j][-1])
                else:
                    memo[curIndex][j] = max(memo[curIndex][j-1], record[curIndex][2] + memo[j][-1])
        return memo[0][-1]
```

New idea here, instead of using ALL possible future paths, store the BEST possible path for everything past this start time, find the closest start time to target's end time, then use that as the result for this record event.

```
class Solution:        
    def jobScheduling(self, startTime, endTime, profit) -> int:
        
        # Construct the data structure for times
        record = sorted(zip(startTime, endTime, profit), key=lambda v: v[0])
        
        """
        Modified Binary Search on the first item of record, find where it would be added and return index
        """
        def binSearch(x):
            left = 0
            right = len(record) - 1
            while right-left > 1:
                mid = (right - left)//2 + left
                
                if record[mid][0] < x:
                    left = mid
                else:
                    right = mid
            return left if record[right][0] >= x else right
            
        # startTime = [record[i][0] for i in range(len(record))]
        @lru_cache
        def f(x):
            
            if x >= len(record):
                return 0
            # First situation, don't add this to the solution
            tempMax = f(x+1)
            
            # This is the profit that MIGHT be added if we do include this
            # toCheck = bisect.bisect_left(startTime, record[x][1])
            
            # Native created function
            toCheck = binSearch(record[x][1]) + 1
            
            tempMax = max(tempMax, record[x][2] + f(toCheck))
            return tempMax
            
        return f(0)
``` 