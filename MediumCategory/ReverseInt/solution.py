class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        min, max =  -2**31, 2**31 - 1

        #store the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed = 0

        while x != 0:
            #pop the last digit from x
            digit = x % 10
            #remove the last digit from x 
            x //= 10

            #check if result is beyond the bounds
            if reversed > (max -digit) // 10:
                return 0

            #add it to result
            reversed = reversed * 10 + digit

        return sign * reversed
