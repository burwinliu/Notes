# Leetcode 764
DP problem with a graph search -- I need to get into the habit of memoing repeated work whenever I see it. Top Down doesn't work due to TLE, but minor setback; with the 2d graph, easily solvable

```
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        record = {tuple(i) for i in mines}
        
        up = [[0 for _ in range(n)] for _ in range(n)]
        left = [[0 for _ in range(n)] for _ in range(n)]
        right = [[0 for _ in range(n)] for _ in range(n)]
        down = [[0 for _ in range(n)] for _ in range(n)]
        
        
        for i in range(n):
            upMin = 1
            downMin = 1
            leftMin = 1
            rightMin = 1 
            for j in range(n):
                rightPos = (i, n-1-j)
                leftPos = (i, j)
                
                upPos = (n-1-j, i)
                downPos = (j, i)
                
                if rightPos in record:
                    rightMin = 0
                if leftPos in record:
                    leftMin = 0
                    
                if upPos in record:
                    upMin = 0
                if downPos in record:
                    downMin = 0
                up[upPos[0]][upPos[1]] = upMin
                down[downPos[0]][downPos[1]] = downMin
                left[leftPos[0]][leftPos[1]] = leftMin
                right[rightPos[0]][rightPos[1]] = rightMin
                upMin += 1
                downMin += 1
                leftMin += 1
                rightMin += 1
        maxOrder = 0
        for i in range(n):
            for j in range(n):
                order = min(up[i][j], left[i][j], right[i][j], down[i][j])
                maxOrder = max(maxOrder, order)
        return maxOrder
        
```