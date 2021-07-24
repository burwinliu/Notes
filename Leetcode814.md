
# Leetcode814
Classic recursion/tree traversal problem. If we were to complicate it with graph potentials, my thinking is we just add some form of record to ensure no overlap, or mark in the variable if space is limited. 

Nothing too scary here though.

```
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left is None and root.right is None and root.val == 0:
            return None
        return root
```