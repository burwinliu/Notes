# Leetcode49
Simple, sort to find key, and use that as way to store values

ALTERNATIVE -- create key with numbers match count, and use that as key; then group via that approach


```
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = {}
        for i in strs:
            key = str(sorted(i))
            if key not in record:
                record[key] = []
            record[key].append(i)
        return record.values()
        
```

```
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = {}
        for i in strs:
            key = self.getKey(i)
            if key not in record:
                record[key] = []
            record[key].append(i)
        return record.values()
    
    
    def getKey(self, inpt):
        res = [0 for _ in range(26)]
        for i in inpt:
            res[ord(i)-97] += 1
        return "/".join([str(i) for i in res])
```