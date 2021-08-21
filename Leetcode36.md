# Leetcode36
The good ol data structures will save us

```
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)] # HashSet {}
        
        for rowNum in range(9): # 0-9
            for colNum in range(9): # 0-9
                cur = board[rowNum][colNum] # Current item based on iterated index
            
                offset = colNum//3
                boxNum = (rowNum//3 * 3) + offset
                
                if cur in rows[rowNum]:
                    return False
                if cur in cols[colNum]:
                    return False
                if cur in boxes[boxNum]:
                    return False
                if cur != ".":
                    rows[rowNum].add(cur)
                    cols[colNum].add(cur)
                    boxes[boxNum].add(cur)
        return True
                
                
        
        
```