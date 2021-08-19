# Leetcode91

A simple-ish dp/search style problem -- count all the possible paths to get to the end.  Kind of like the steps problems (can take 1 or 2 steps to the end) except, this has another condition (can only be 10s OR 20-26) and 0s being an insta lose. 


```
class Solution:
    def numDecodings(self, s: str) -> int:
        pos = [0 for _ in range(len(s) + 1)]
        pos[0] = 1
        i = 0
        while i < len(s):
            print(i)
            pos[i+1] += pos[i]
            if s[i] == "1":
                if i + 1 != len(s):
                    pos[i+2] += pos[i]

                    if s[i+1] == '0':
                        i += 2
                        continue
            elif s[i] == "2":
                if i + 1 != len(s) and int(s[i+1]) <= 6:
                    pos[i+2] += pos[i]
                    if s[i+1] == '0':
                        i += 2
                        continue
            elif s[i] == "0":
                return 0
            i += 1
        return pos[len(s)]
```