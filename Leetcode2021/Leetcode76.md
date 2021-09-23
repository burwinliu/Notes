# Leetcode76
Definitely not the cleanest thing out there. However, it works -- sliding window, with a moving forwards pointer, and if we hit the entire substring, then move back until RIGHT BEFORE it no longer is -- then iterate that back forwards, and move forawrds until we get a new cover. This works as we would find the minimum possible cover for every section of the string that would produce the substring, and by doing it with the sliding window, its O(m+n)
```
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        tracker = {}
        for i in t:
            if i not in tracker:
                tracker[i] = 0
            tracker[i] += 1
        
        
        p1 = 0
        p2 = 0
        tracked = len(t)
        
        output = None
        while p1 < len(s):
            if s[p1] in tracker:
                tracker[s[p1]] -= 1
                if tracker[s[p1]] >= 0:
                    tracked -= 1
            if tracked == 0:
                while p2 <= p1:
                    if s[p2] in tracker:
                        tracker[s[p2]] += 1
                        if tracker[s[p2]] == 1:
                            if output is None or len(output) > p1 - p2 + 1:
                                output = s[p2:p1+1]
                            p2 += 1
                            tracked += 1
                            break
                    p2 += 1
            p1 += 1
        while tracked == 0 and p2 <= p1:
            if s[p2] in tracker:
                if tracker[s[p2]] == 0:
                    if output is None or  len(output) > p1 - p2 + 1:
                        output = s[p2:p1+1]
                    break
                tracker[s[p2]] += 1
            p2 += 1
        if output is None:
            return ""
        return output
```