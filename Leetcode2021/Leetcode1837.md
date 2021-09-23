# Leetcode1837
While loop and some math -- just keep going and remember to add the proper amount for result

```
class Solution:
    def sumBase(self, n: int, k: int) -> int: 
        
        result = 0
        cur = 1
        
        while n != 0:
            result += (n % (cur * k))//cur
            cur *= k
            n -= n % cur
        return result
```