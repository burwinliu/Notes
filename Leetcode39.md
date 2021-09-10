# Leetcode39

Well well.. here we are again. BFS with the possible values and sort to ensure unique values.


```
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        q = [[[], 0]]
        result = set()
        
        
        while len(q) != 0:
            curRes, total = q.pop()
            
            for i in candidates: 
                # Over
                if total + i > target:
                    continue
                curResCopy = [i for i in curRes]
                curResCopy.append(i)
                
                # Equal, good result
                if total + i == target:
                    result.add(tuple(sorted(curResCopy)))
                else:
                    # Still might be 
                    q.append([curResCopy, total + i])
        return [list(i) for i in result]
        
```