# Leetcode153
Good ol fashion binary search. The logic threw me a bit for a loop to find the correct condition to assign, but got it in the end.


```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while right - left > 1:
            mid = (right - left) // 2 + left
            
            if (nums[mid] > nums[right] and nums[mid] > nums[left]): 
                left = mid 
            else:
                right = mid
        return min(nums[left], nums[right])
```