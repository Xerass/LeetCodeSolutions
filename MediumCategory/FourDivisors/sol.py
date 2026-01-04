import math 
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #utilize the sqrt approach cuz im too dumb to use prime factorization
        # this should be good enough as max num is only 100k at most we only do 316 operations

        def findDivisors(num):
            #every divisor is unique (except a square root but we will consider it later)
            #so, we dont even need to setup a set() since its guaranteed they wont show up again
            divisors = []
            #from one to the sqrt of the number:
            for i in range(1, int(math.sqrt(num) + 1)):
                if num % i == 0:
                    divisors.append(i)
                    if i * i != num: #avoid perfect squares
                        #int div so everything stays as a div (python is absolutely annoying with /)
                        divisors.append(num//i)

            #return the list
            return divisors

        sumTotal = 0
        for num in nums:
            candidate = findDivisors(num)
            if len(candidate) == 4:
                total = sum(candidate)
                sumTotal += total

        return sumTotal
