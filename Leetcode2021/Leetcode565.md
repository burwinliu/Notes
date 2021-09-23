# Leetcode565

Since we take advantage of the unique situation of each input, we don't need to consider the possibility of loops or multiple entries into a loop to cause a more optimal solution to be found -- therefore once visited, don't need to visit again (can't have a mini loop within the larger loop as everything's unique, and can't have two entries to a loop)

```
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        record = [False for _ in nums]
        
        count = 0
        
        for pos, val in enumerate(nums):
            
            if record[pos]:
                continue
            # b/c unique, just need to track once; once visited, don't need to track again.
            temp = val
            tmpCount = 1
            while temp != pos:
                record[temp] = True
                temp = nums[temp]
                tmpCount += 1
            
            count = max(tmpCount, count)
        return count
```