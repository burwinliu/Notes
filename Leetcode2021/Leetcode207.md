# Leetcode207

Fairly clear to be a DFS problem, find the cycles and all that

Issue -- trying to find cycles in iterative manner might be a bit more tricky.

```
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {}
        toTraverse = set()
        for i in prerequisites:
            if i[0] not in preReq:
                preReq[i[0]] = list()
            preReq[i[0]].append(i[1])
            toTraverse.add(i[0])
            
        store = set()
        
        @lru_cache(None)
        def findLoop(start):
            if start in store:
                return True
            if start not in preReq:
                return False
            store.add(start)
            for i in preReq[start]:
                if findLoop(i):
                    return True
            store.remove(start)
            return False
            
        for i in preReq.keys():
            if findLoop(i):
                return False
                
        return True
```