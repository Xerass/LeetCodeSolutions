class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #newton raphson method

        if x < 2:
            return x
        
        guess = x

        while guess * guess > x:
            # Newton's iteration: x_{n+1} = (x_n + a / x_n) / 2
            guess = (guess + x // guess) // 2

        return guess
