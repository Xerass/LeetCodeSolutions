class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        #if x is negative, ends in 0 and is not 0 it is never a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        #build the reversed half:
        reversed = 0
        while x > reversed:
            reversed = reversed * 10 + x%10
            #integer div to remove remainders
            x //= 10
        
        #check if reversd half = original half
        #integer div odd length numbers to remove the excess digit (should have been shared by both nums anyways)
        return x == reversed or x == reversed // 10
