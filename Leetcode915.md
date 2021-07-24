# Leetcode915
Felt like a greedy problem at first
The thinking went, as long as everything is greater then the max behind me, we can greedily say, this is the best partition. HOWEVER once we saw something less, then everything before became the parition, and we must start over again. This would continue to work throughout, regardless of where the partition is, as per the rules of the paritioning.

```
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        size = 1
        leftGreaterThen = nums[0]
        rightMaxThusFar = -1
        for i in range(1, len(nums)):
            if nums[i] >= leftGreaterThen:
                rightMaxThusFar = max(rightMaxThusFar, nums[i])
            else:
                leftGreaterThen = max(leftGreaterThen, rightMaxThusFar)
                size = i + 1
        return size
```