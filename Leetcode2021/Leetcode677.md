# Leetcode677
Brute Force solution with hash keys and search. A better way to do this would be a trie (will implement and use later) with dictionary to remove all if found, and if not found, add to all items along the way -- then on retrieve, navigate to correct trie node.

```
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record = {}
        
        

    def insert(self, key: str, val: int) -> None:
        self.record[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for i in self.record.keys():
            val = 0
            while val != len(prefix) and val != len(i) and prefix[val] == i[val]:
                val += 1
            if val == len(prefix):
                res += self.record[i]
        return res
```