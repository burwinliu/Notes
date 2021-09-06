# Leetcode899
Well, well, well.. My first Hard without assistance in some time

However, this is one that is more devious then anything; its not inherintly difficult. The idea is that with 2, you can swap and reorder each letter to the proper position (a la bubble sort) but, with 1, just find the minimal possible position in the string; just requires some thinking about the solution

```
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        tmp = min(s)
        res = s
        
        for i in range(len(s)):
            if s[i] == tmp:
                res = min(res, s[i:] + s[:i])
        return res
```