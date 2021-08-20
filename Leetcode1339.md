# Leetcode1339

Remember to read the instructions carefully -- the modulo no lie actually spent me 20 minutes to find out as the reason why I failed test cases

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = 0 
        q = [root]
        while len(q) != 0:
            cur = q.pop()
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
            total += cur.val
        
        def helper(node):
            maxThusFar = 0
            curTotal = node.val
            if node.left is not None:
                left = helper(node.left)
                maxThusFar = max((total - left[0])*left[0], maxThusFar, left[1])
                curTotal += left[0]
            if node.right is not None:
                right = helper(node.right)
                maxThusFar = max((total - right[0])*right[0], maxThusFar, right[1])
                curTotal += right[0]
            return [curTotal, maxThusFar]
        return helper(root)[1] % (10**9+7)
        
        
        
```