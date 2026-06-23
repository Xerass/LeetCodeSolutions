class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #this literally just reads as fibonacci number
        #lets assume we start at the top so fib makes more sense
        #if we can only take 1 or 2 steps, we simply take both pahts and add them up
        #(n-1) + (n-2) -> at each level
        #we simply iterate from n to figure out its fibonacci number

        #cached, cache is a fict that stores the value per n
        #climbing 0 (1) is still 1 way, so we add that
        def fib(n, cache = {0: 1, 1: 1}):
            if n not in cache:
                cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
            return cache[n]

        
        return fib(n)
