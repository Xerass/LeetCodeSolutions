class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #cool trick, binary addition is simply a XOR of two nums added to the AND of two nums (shifted left once, to simulate a carry)
        #XOR works exactly how it would in an adder 0 + 0 = 0 1 + 1 = 0 1 + 0 = 1 0 + 1 = 1, the and shifted left simply checks if 1,1 and pushes a one to the left, to simulate a carry
        #specify base 2
        a = int(a, 2)
        b =  int(b, 2)
        while b != 0:#while b can still have carries, keep doing this
            base = (a ^ b)
            #bit shift left to simulate carry
            carry = (a & b) << 1

            a = base
            b = carry

        #when b is 0, XOR should have the final sum.
        return bin(a)[2:]
