# Leetcode542
Quite the tricky BFS problem. Instead of starting from one position, start from all 0s to ensure that minimal distance is found at once (as this allows for you to start from every position, and spread out, hitting min distance asap). I need to broaden my thinking in regards to these problem solutions.

```
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        record = []
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    record.append((i, j))
                else:
                    mat[i][j] = None
        while len(record) != 0:
            cur = record.pop(0)
            if cur[0]+1 != len(mat):
                if mat[cur[0] + 1][cur[1]] is None or mat[cur[0] + 1][cur[1]] > mat[cur[0]][cur[1]] + 1:
                    mat[cur[0] + 1][cur[1]] =  mat[cur[0]][cur[1]] + 1
                    record.append((cur[0] + 1, cur[1]))
            if cur[0]-1 != -1:
                if mat[cur[0] - 1][cur[1]] is None or mat[cur[0] - 1][cur[1]] > mat[cur[0]][cur[1]] + 1:
                    mat[cur[0] - 1][cur[1]] =  mat[cur[0]][cur[1]] + 1
                    record.append((cur[0] - 1, cur[1]))
            if cur[1]+1 != len(mat[0]):
                if mat[cur[0]][cur[1]+1] is None or mat[cur[0]][cur[1]+1] > mat[cur[0]][cur[1]] + 1:
                    mat[cur[0]][cur[1]+1] =  mat[cur[0]][cur[1]] + 1
                    record.append((cur[0], cur[1]+1))
            if cur[1]-1 != -1:
                if mat[cur[0]][cur[1]-1] is None or mat[cur[0]][cur[1]-1] > mat[cur[0]][cur[1]] + 1:
                    mat[cur[0]][cur[1]-1] =  mat[cur[0]][cur[1]] + 1
                    record.append((cur[0], cur[1]-1))
        return mat
```
        