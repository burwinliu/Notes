# Leetcode16
The famous 3 sum -- varied.

I had some trouble figuring out how to do closest -- but for these cases, sorted stuff is your friend -- you can take advantage of the sort and two pointers inwards to find the best combo with a moving pointer up.
    * This takes advantage of 2 sum closest -- 
        * if a sum is larger, then we know that that item must be too big on one side, therefore discard and move inwards -- if we increase on the other side, we will always be getting further away. 
        * If too small, increase on the left side -- as we want to get closer and closer (as this is the smallest amount we can change by, while getting closer or overshooting). 
    * However, is it possible to move the pointers, and then "lose" the optimal solution? 
        * No -- as if it were, we would have found it using the smallest increment available from the left hand side
            * However, what if we already iterated over it in some prior iteration? Well, think of the following: (let the left hand pointer value be p1, and right hand pointer value be p2)
                * FOR something to increase on the left hand side, nums[p2] + nums[px] s.t x is < p1, must have been smaller then target
                * therefore, if we increase px -> p1, then we know that px would have been too small for all py, s.t y is some future possibility of p2. Therefore, we can safely iterate p1 up and p2 down, discarding along the way

There was a binary search solution on leetcode, something to add to this write up in the future
```
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        close = None
        for i, val in enumerate(nums):
            
            p1 = i + 1
            p2 = len(nums) - 1
            
            while p1 < p2:
                if close is None or abs(target - close) > abs(target - (val + nums[p2] + nums[p1])):
                    close = (val + nums[p2] + nums[p1])
                if target - (val + nums[p2] + nums[p1]) <= 0:
                    p2 -= 1
                else:
                    p1 += 1
        return close
```