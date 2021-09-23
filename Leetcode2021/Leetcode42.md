# Leetcode 42

One I did myself, but its needlessly complex. Need to look back and optimize this approach.. a lot

```
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [[-1, 0]]
        trapped = 0 
        pos = 0
        
        while pos < len(height):
            while pos < len(height) and len(stack) == 1 and height[pos] >= stack[-1][1]:
                stack[0] = [pos, height[pos]]
                pos += 1
            if pos < len(height):
                if height[pos] < stack[-1][1]:
                    stack.append([pos, height[pos]])
                elif height[pos] == stack[-1][1]:
                    stack[-1][0] = pos
                else:
                    floor = stack[-1][1]
                    while len(stack) != 0 and height[pos] >= stack[-1][1]:
                        cur = stack.pop(len(stack)-1)
                        trapped += (cur[1] - floor) * (pos - cur[0] - 1)
                        floor = cur[1]
                    if len(stack) != 0:
                        trapped += (height[pos] - floor) * (pos - stack[-1][0] - 1)
                    stack.append([pos, height[pos]])
            pos += 1
        return trapped
        # while pos < len(height):
        #     if len(stack) != 0 and j < stack[-1][1]:
        #         stack.append((i, j))
        #     while len(stack) != 0 and j >= stack[-1]:
```