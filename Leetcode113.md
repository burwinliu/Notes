# Leetcode113

Standard Tree traversal, find the solution -- recursion makes the most sense. can improve via BFS/DFS  (need to search all, can minimize space required to search + improve  (no need for stack and cost of recursion in python, etc.)

```

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        if targetSum-root.val == 0 and root.left is None and root.right is None:
            res.append([root.val])
        for i in self.pathSum(root.left, targetSum-root.val):
            res.append([root.val] + i)
        for i in self.pathSum(root.right, targetSum-root.val):
            res.append([root.val] + i)
        return res
```