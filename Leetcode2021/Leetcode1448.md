# Leetcode1448
Standrad BFS/DFS problem; a fairly standrard affair of recourd and count

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        q = [[root, -10**4 - 1]]
        while len(q) != 0:
            cur = q.pop()
            if cur[1] <= cur[0].val:
                count += 1
                cur[1] = cur[0].val
            
            if cur[0].left != None:
                q.append([cur[0].left, cur[1]])
            if cur[0].right != None:
                q.append([cur[0].right, cur[1]])
        return count
```