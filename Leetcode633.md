# Leetcode633
This is a q uick and dirty way. The reason it works is as follows:
    * If currently, the value is larger, the sum will decrease from the less specific side, as trying the other side of things (increasing the head pointer) is useless -- it will eternally be larger.
    * If currently, the total is smaller, then I can keep trying to increase the more specific side (the small pointer) to get to the value, until I reach case 1
    * At this current value, I know that all values before me on the large end have already been tried until they surpass; and on the smaller side, it was already tried with something closer in value that eventually was not found to be matching (as if it was too large on the sum, they would've moved the pointer away).
    * THEREFORE -- all valid values are tried.

```
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int(c**(.5))
        
        while low <= high:
            total = low**2 + high ** 2 
            if total == c:
                return True
            elif total < c:
                low += 1
            else:
                high -= 1
        return False
```