class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_len = 0x7FFFFFFF
        mask = 0xFFFFFFFF

        while b != 0: 
            carry = (a & b) << 1 # getting carry and shifting to the left
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_len else ~(a^mask)
        
        