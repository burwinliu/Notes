# Leetcode330
The good ol fashion greedy algo.

In this instance, coverage is the name of the game -- try and extend coverage as much possible with the principle that (if I can cover from 0..n, and I add n+1, I can cover to 2n+1) and the idea that (if I can cover from 0..n, and I have n+2, I must add n+1, but may cover to 2n+2).

This is minimal as we maximize coverage area, with the least amount of numbers, so 2 for 1 homerun for greedy.

```
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        point = 0
        coverage = 0
        result = 0
        
        while coverage < n: 
            if point < len(nums) and nums[point] <= coverage + 1:
                coverage = coverage + nums[point]
                point += 1
            else:
                result += 1
                coverage = 2 * coverage + 1
        return result
                
```