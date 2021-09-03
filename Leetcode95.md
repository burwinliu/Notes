# Leetcode95
Standard recursion stuff. To improve, we can use a tuple and use @lru_cache for efficiencies sake.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        toPass = [i for i in range(1, n+1)]
        def genFrom(possible):
            res = []
            for i in range(len(possible)):
                rightSplit = possible[i+1:]
                leftSplit = possible[:i]
                rightNodes = genFrom(rightSplit)
                leftNodes = genFrom(leftSplit)
                for right in rightNodes:
                    for left in leftNodes:
                        res.append(TreeNode(val=possible[i], left=left, right=right))
            if len(res) == 0:
                return [None]
            return res
        return genFrom(toPass)
            
```