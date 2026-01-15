class Solution:
    def isHappy(self, n: int) -> bool:
        #a happy number is a digit whose sum of the squares of its digit is 1 (after looping till it reaches one)

        #to consider the infinite nature, we need to create a set
        #if num already in set but was not = 1 this must mean its infiinite
        seen = set()

        while n!=1 and n not in seen:
            seen.add(n)

            #process n
            #raaaah 
            n = sum(int(digit) ** 2 for digit in str(n))
        
        return n == 1
