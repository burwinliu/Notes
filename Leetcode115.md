# Leetcode115
Typical DP style problem -- things to note is the fact that lru_cache requires () to setup

```
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @lru_cache(None)
        def helper(posS, posT):
            if posT == len(t):
                return 1
            if posS == len(s):
                return 0
            if s[posS] == t[posT]:
                return helper(posS + 1, posT + 1) +  helper(posS + 1, posT)
            return helper(posS + 1, posT)
        return helper(0, 0)
```