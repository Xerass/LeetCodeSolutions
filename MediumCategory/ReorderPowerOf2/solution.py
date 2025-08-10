class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #to count instances ofthe nums
        from collections import Counter

        counts = Counter(str(n))

        powers = [Counter(str(1 << i)) for i in range(31)]

        return counts in powers

