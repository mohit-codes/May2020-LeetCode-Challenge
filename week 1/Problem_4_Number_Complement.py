# Given a positive integer num, output its complement number. 
# The complement strategy is to flip the bits of its binary representation.

# Naive Solution
	
class Solution:
    def findComplement(self, num: int) -> int:
        y = bin(num)[2:]
        x = ""
        for i in range(len(y)):
            if y[i] == '1': x = x +"0"
            else: x=x+"1"
        return int(x,2)
