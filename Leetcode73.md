# Leetcode73
Simple using None situation with python.

the true better answer is to flag the rows and cols, and use two vars to mark the first rows, but.. I didn't think of that when solving this.


```
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = None
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = None
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        return matrix
```