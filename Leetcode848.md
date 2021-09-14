# Leetcode848

Prefix sum style problem, just carry sum as you go through the problem and set proper value as you go along.

```
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = ""
        
        count = 0 
        base = ord("a")
        
        for i in range(len(s)):
            count = (count + shifts[-1-i]) % 26
            cur = chr(((ord(s[-1-i]) - base) + count) % 26 + base)
            res = cur + res
        return res
```