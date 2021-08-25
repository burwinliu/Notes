# Leetcode537
This is not a medium -- just parsing
```
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        toParse1 = [i.strip() for i in num1.split("+")]
        toParse2 = [i.strip() for i in num2.split("+")]
        
        real1 = int(toParse1[0])
        real2 = int(toParse2[0])
        
        imaginary1 = int(toParse1[1][:-1])
        imaginary2 = int(toParse2[1][:-1])
        
        realTotal = real1 * real2 + -1 * (imaginary1 * imaginary2)
        
        imaginaryTotal = real1 * imaginary2 + real2 * imaginary1
        
        return f"{realTotal}+{imaginaryTotal}i"
```