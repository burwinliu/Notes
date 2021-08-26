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