# Leetcode522
Pretty annoying question.

The main idea of this one is to realize that -- for something to be the longest uncommon subsequence, it must unique, and must not be the subsequence of anything longer.

First, sort everything by length, and in each length, count how many occurances of a string occurs. If its 1, if its the longest, then return that length. else check if its a substring of any of the longest strings, if not return its length

Finally, if nothing passes and returns early, return -1.

```
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        record = {}
        for i in strs:
            if len(i) not in record:
                record[len(i)] = []
            record[len(i)].append(i)
        search = sorted(record.keys(), reverse=True)
        toCheck = None
        for length in search:
            record2 = {}
            for i in record[length]:
                if i not in record2:
                    record2[i] = 0
                record2[i] += 1
            for i in record2.keys():
                if record2[i] == 1:
                    if toCheck is None:
                        return length
                    res = True
                    for check in toCheck:
                        res = res and not self.isSub(check, i)
                    if res:
                        return length                    
                    
            if toCheck is None:
                toCheck = record2.keys()
        return -1
    
    @lru_cache()
    def isSub(self, longer, shorter):
        if longer is None:
            return False
        pLong = -1
        for i in shorter:
            pLong += 1
            while pLong != len(longer) and longer[pLong] != i:
                pLong += 1
                
            if pLong == len(longer):
                return False
        return True
```