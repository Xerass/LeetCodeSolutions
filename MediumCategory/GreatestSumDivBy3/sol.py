class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = 0
        rem1First = float('inf')
        rem2First = float('inf')
        rem1Sec = float('inf')
        rem2Sec = float('inf')

        #iter, adding curr sum, taking note of last 2 lowest of each
        for num in nums:
            currSum += num
            if num % 3 == 1:
                if num < rem1First:
                    rem1Sec = rem1First
                    rem1First = num
                elif num < rem1Sec:
                    rem1Sec = num
            if num % 3 == 2:
                if num < rem2First:
                    rem2Sec = rem2First
                    rem2First = num
                elif num < rem2Sec:
                    rem2Sec = num    

        toRemove = 0

        if currSum % 3 == 1:
            if (rem2Sec + rem2First) < rem1First:
                toRemove = rem2Sec + rem2First
            else:
                toRemove = rem1First
        elif currSum % 3 == 2:
            if (rem1Sec + rem1First) < rem2First:
                toRemove = rem1Sec + rem1First
            else:
                toRemove = rem2First

        print(toRemove)

        return currSum - toRemove

    
