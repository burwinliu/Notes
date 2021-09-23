# Leetcode523

Standard prefix sum -- use mod to ensure multiple is accepted

```
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixRecord = set()
        holder = 0
        current = 0
        for i in range(len(nums)):
            if i > 1:
                holder += nums[i-2]
                prefixRecord.add(holder % k)
            current += nums[i]
            if (current % k == 0 and i >= 1) or (current % k) in prefixRecord:
                return True
        return False
```