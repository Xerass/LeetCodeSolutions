class Solution:
    def hammingWeight(self, n: int) -> int:
        #unholy bitwise operations
        #use a population count approach

        #we count bits at 2,4,8,16,32 bit fields at a tmie, adding each, then it should return total

        n =((n & 0xAAAAAAAA) >> 1) + (n & 0x55555555)
        n =((n & 0xCCCCCCCC) >> 2) + (n & 0x33333333)
        n =((n & 0xF0F0F0F0) >> 4) + (n & 0x0F0F0F0F)
        n =((n & 0xFF00FF00) >> 8) + (n & 0x00FF00FF)
        n =((n & 0xFFFF0000) >> 16) + (n & 0x0000FFFF)
        
        return int(n)
