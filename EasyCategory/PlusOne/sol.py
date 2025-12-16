class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        #go from the back add 1 if sum > 9 set val to 0 and add 1 to next, keep doing that.
        n = len(digits)

        #note, stop is exclusive so -1 stops at 0
        for i in range(n - 1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits

            #if digit is a 9 make it 0
            digits[i] = 0

            #if we reached this case, where i is 0, must mean we reached the end with all 9's, add a 1 at the front
            if i == 0:
                digits.insert(0,1)
        
        return digits

            
