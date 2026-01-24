class Solution:
    def climbStairs(self, n: int) -> int:
        #we can approach this with a memoization, top down technique
        
        #catch cases where n <= 2:
        if n <= 2:
            #we know we can only use the exact same amount of steps
            #n = 1 can use step [1]
            #n = 2 can use step[[1,1], [2]]
            #so just return n
            return n

        #we know that to reach say step 10, we can only ever be at step 8 or 9
        #so if we add both of them, we can get the different ways to get to step 10
        #this applies to all i, as such we only ever need the previous 2 values

        #represents the very first steps, n=1 and n=2, from there grow the steps
        first, second = 1, 2

        #start at 3 since 1 and 2 are covered
        for i in range(3, n + 1):
            current = first + second
            #move current to second, second to first
            first = second
            second = current
        
        return second
