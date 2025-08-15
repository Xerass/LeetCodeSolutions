class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (
            n > 0 and
            (n & (n - 1)) == 0 and           # check power of two
            (n & 0x55555555) != 0            #a power of 4 has a 1 in an evem bit and nowhere else, cross with the number above which is a bin where every odd bit is 1 so we can compare.
        )
