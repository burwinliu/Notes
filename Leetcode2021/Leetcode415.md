# Leetcode 415
Nothing terribly interesting -- there is a world if you need to, you can convert it ALL to strings, use dict
 to efficiently add, and not use any integers, but its a bit of a pain. you would need to recurse the carry over as well... really not worth the time
 

```
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        toAddLen = min(len(num1), len(num2))
        carry = 0
        res = ""
        
        for i in range(1, toAddLen+1):
            pos = -1 * i
            cur = str(int(num1[pos]) + int(num2[pos]) + carry)
            if len(cur) == 2:
                carry = int(cur[0])
                res = cur[1] + res
            else:
                res = cur + res
                carry = 0
        if len(num1) != len(num2):
            if len(num1) > len(num2):
                return str(int(num1[0:-toAddLen]) + carry) + res
            else:
                return str(int(num2[0:-toAddLen]) + carry) + res
        else:
            if carry == 0:
                return res
            return str(carry) + res
            
        
```
